from django.contrib import admin

from vaultsrv.models import (
    Account, AccountGroup, GroupMembership, Customer, ServiceGroup, Service,
    ServiceGroupMembership
)

# This is no the final admin definition, it's is only to test the models
admin.site.register((
    Account, AccountGroup, GroupMembership, Customer, ServiceGroup, Service,
    ServiceGroupMembership
))
