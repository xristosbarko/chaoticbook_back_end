from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


account_activation_token = TokenGenerator()


# def sendVerificationEmail(request, user):
#     current_site = get_current_site(request)
#     mail_subject = "Activate your account."
#     message = render_to_string(
#         "email_verification.html",
#         {
#             "user": user,
#             "domain": current_site.domain,
#             "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#             "token": account_activation_token.make_token(user),
#         },
#     )
#     to_email = form.cleaned_data.get("email")
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     email.send()
