from django.contrib.auth import authenticate

import graphene
from graphene import ObjectType, Field
import graphql_jwt
from graphql_jwt.shortcuts import get_token
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.decorators import login_required


from ...core.models import User, OTP
from .types import UserNode


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = Field(UserNode)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class RequestOTP(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        phone_number = graphene.String(required=True)

    @classmethod
    def mutate(self, info, username):
        user = User.objects.get(phone_number=username)
        OTP.objects.create(
            user=user,
        )
        return RequestOTP(status="success")


class VerifyOTP(graphene.Mutation):
    status = graphene.String()
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        phone_number = graphene.String(required=True)
        otp_message = graphene.String(required=True)

    def mutate(self, info, phone_number, otp_message):
        user_obj = User.objects.get(phone_number=phone_number)
        related_otp = OTP.objects.filter(user=user_obj, is_valid=True)
        for otp in related_otp:
            if otp.message == otp_message and otp.is_valid == True:
                otp.valid = False
                otp.save()
                token = get_token(user_obj)
                refresh_token = create_refresh_token(user_obj)
                # user_obj.is_verified = True
                # user_obj.save()
                return VerifyOTP(status="success", token=token, refresh_token=refresh_token)
        return VerifyOTP(status="failed", token=None, refresh_token=None)


# veridy user by 
class VerifyUser(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        pass

    @login_required
    def mutate(self, info):
        try:
            user = info.contex.user
            user.is_verified = True
            user.save()
            return VerifyUser(status="success")
        except:
            return VerifyUser(status="failed")



# change password
class ChangePassword(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        old_password = graphene.String(required=True)
        new_password = graphene.String(required=True)

    @login_required
    def mutate(self, info, old_password, new_password):
        user = authenticate(phone_number=info.context.user.phone_number, password=old_password)
        if user:
            user.set_password(new_password)
            user.save()
        else:
            return ChangePassword(status="failed, prev password is not True")
        return ChangePassword(status="success")


class ChangePasswordAfterOTPVerified(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        new_password = graphene.String()

    @login_required
    def mutate(self, info, new_password):
        try:
            user = info.context.user
            user.set_password(new_password)
            user.save()
            return ChangePasswordAfterOTPVerified(status="success")
        except:
            return ChangePasswordAfterOTPVerified(status="failed")



class CoreMutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    request_otp = RequestOTP.Field()
    verify_OTP = VerifyOTP.Field()
    change_password = ChangePassword.Field()
    Chnage_password_after_otp_verified = ChangePasswordAfterOTPVerified.Field()
