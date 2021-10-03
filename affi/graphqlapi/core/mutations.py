import graphene
from graphene import ObjectType, Field
import graphql_jwt

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


class VerifyUser(graphene.Mutation):
    status = graphene.String()

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
                user_obj.is_verified = True
                user_obj.save()
                return VerifyUser(status="success")
        return VerifyUser(status="failed")


class CoreMutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    request_otp = RequestOTP.Field()
    verify_user = VerifyUser.Field()
