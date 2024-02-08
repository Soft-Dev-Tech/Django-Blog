
class Publish():
    def make_published(self, request, queryset):
        updated = queryset.update(status="pb")
        if updated == 1:
            message = "1 Article"
        else:
            message = "%s Articles were" % updated
        self.message_user(
            request, "%s Successfully marked as Published." % message)

    make_published.short_description = "Mark selected articles as Published"


class Draft():
    def make_draft(self, request, queryset):
        updated = queryset.update(status="d")
        if updated == 1:
            message = "1 Article"
        else:
            message = "%s Articles were" % updated
        self.message_user(
            request, "%s Successfully marked as Draft." % message)

    make_draft.short_description = "Mark selected articles as Draft"

class Pending():
    def make_pending(self, request, queryset):
        updated = queryset.update(status="pd")
        if updated == 1:
            message = "1 Article"
        else:
            message = "%s Articles were" % updated
        self.message_user(
            request, "%s Successfully marked as Pending." % message)

    make_pending.short_description = "Mark selected articles as Pending"


class Back():
    def make_back(self, request, queryset):
        updated = queryset.update(status="b")
        if updated == 1:
            message = "1 Article"
        else:
            message = "%s Articles were" % updated
        self.message_user(
            request, "%s Successfully marked as Back." % message)

    make_back.short_description = "Mark selected articles as Back"


class Active():
    def active(self, request, queryset):
        updated = queryset.update(status=True)
        if updated == 1:
            message = "1 Category"
        else:
            message = "%s Categories were" % updated

        self.message_user(request, "%s successfully made as active." % message)
    
    active.short_description = "Mark selected categories as Active"


class Passive():
    def passive(self, request, queryset):
        updated = queryset.update(status=False)
        if updated == 1:
            message = "1 Category"
        else:
            message = "%s Categories were" % updated
        self.message_user(
            request, "%s successfully made as passive." % message)

    passive.short_description = "Mark selected categories as Passive"
