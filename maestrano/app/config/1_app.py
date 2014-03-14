# Get full host (protocal + server host)
#protocol = ('https://' if (('HTTPS' in os.environ['SERVER_PROTOCOL'])) else 'http://')
full_host = 'http://localhost:8069'

# Name of your application
mno_settings.app_name = 'my-app'

# Enable Maestrano SSO for this app
mno_settings.sso_enabled = True

# SSO initialization URL
mno_settings.sso_init_url = full_host + '/maestrano/auth/saml/index'

# SSO processing url
mno_settings.sso_return_url = full_host + '/maestrano/auth/saml/consume'
