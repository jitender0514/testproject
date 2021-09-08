import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from business.models import Businesses
from django.contrib.auth.models import User
from graphql_relay.node.node import from_global_id



class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ["username", "first_name", "last_name"]
        interfaces = (relay.Node,)


class BusinessesType(DjangoObjectType):
    class Meta:

        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        model = Businesses
        interfaces = (relay.Node,)


class Query:
    user = relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)

    business = relay.Node.Field(BusinessesType)
    all_business = DjangoFilterConnectionField(BusinessesType)


class UpdateBusiness(graphene.Mutation):
    """Mutation for updating user profile. Login is required with JWT in Authorization header"""
    business = graphene.Field(BusinessesType)

    class Arguments:
        name = graphene.String()
        id = graphene.ID()

    def mutate(cls, info, name, id):
        # get the current user from context
        id = from_global_id(id)[1]
        business = Businesses.objects.get(pk=id)
        business.name = name
        business.save()
        return UpdateBusiness(business=business)


class businessInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    employee_size = graphene.Int(required=True)
    owner = graphene.ID(required=True)


class CreateBusiness(graphene.Mutation):
    """Mutation for updating user profile. Login is required with JWT in Authorization header"""
    business = graphene.Field(BusinessesType)

    class Arguments:
        business_data = businessInput(required=True)

    def mutate(cls, info, business_data=None):
        # get the current user from context
        owner_id = from_global_id(business_data.owner)[1]
        business = Businesses.objects.create(
            name=business_data.name, address=business_data.address, employee_size=business_data.employee_size, owner_id=owner_id
        )
        return CreateBusiness(business=business)


class DeleteBusiness(graphene.Mutation):
    """Mutation for updating user profile. Login is required with JWT in Authorization header"""
    business = graphene.Field(BusinessesType)

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info,  id):
        # get the current user from context
        id = from_global_id(id)[1]
        business = Businesses.objects.get(id=id)
        business.delete()
        print(business)
        return DeleteBusiness(business=business)


class Mutation(graphene.ObjectType):
    update_business = UpdateBusiness.Field()
    create_business = CreateBusiness.Field()
    delete_business = DeleteBusiness.Field()
