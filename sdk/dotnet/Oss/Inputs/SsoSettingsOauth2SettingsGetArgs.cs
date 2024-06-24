// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Oss.Inputs
{

    public sealed class SsoSettingsOauth2SettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If enabled, it will automatically sync the Grafana server administrator role.
        /// </summary>
        [Input("allowAssignGrafanaAdmin")]
        public Input<bool>? AllowAssignGrafanaAdmin { get; set; }

        /// <summary>
        /// If not enabled, only existing Grafana users can log in using OAuth.
        /// </summary>
        [Input("allowSignUp")]
        public Input<bool>? AllowSignUp { get; set; }

        /// <summary>
        /// List of comma- or space-separated domains. The user should belong to at least one domain to log in.
        /// </summary>
        [Input("allowedDomains")]
        public Input<string>? AllowedDomains { get; set; }

        /// <summary>
        /// List of comma- or space-separated groups. The user should be a member of at least one group to log in. For Generic OAuth, if you configure allowed*groups, you must also configure groups*attribute_path.
        /// </summary>
        [Input("allowedGroups")]
        public Input<string>? AllowedGroups { get; set; }

        /// <summary>
        /// List of comma- or space-separated organizations. The user should be a member of at least one organization to log in.
        /// </summary>
        [Input("allowedOrganizations")]
        public Input<string>? AllowedOrganizations { get; set; }

        /// <summary>
        /// The user information endpoint of your OAuth2 provider. Required for okta and generic_oauth providers.
        /// </summary>
        [Input("apiUrl")]
        public Input<string>? ApiUrl { get; set; }

        /// <summary>
        /// It determines how client*id and client*secret are sent to Oauth2 provider. Possible values are AutoDetect, InParams, InHeader. Default is AutoDetect.
        /// </summary>
        [Input("authStyle")]
        public Input<string>? AuthStyle { get; set; }

        /// <summary>
        /// The authorization endpoint of your OAuth2 provider. Required for azuread, okta and generic_oauth providers.
        /// </summary>
        [Input("authUrl")]
        public Input<string>? AuthUrl { get; set; }

        /// <summary>
        /// Log in automatically, skipping the login screen.
        /// </summary>
        [Input("autoLogin")]
        public Input<bool>? AutoLogin { get; set; }

        /// <summary>
        /// The client Id of your OAuth2 app.
        /// </summary>
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("clientSecret")]
        private Input<string>? _clientSecret;

        /// <summary>
        /// The client secret of your OAuth2 app.
        /// </summary>
        public Input<string>? ClientSecret
        {
            get => _clientSecret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _clientSecret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("custom")]
        private InputMap<string>? _custom;

        /// <summary>
        /// Custom fields to configure for OAuth2 such as the [force*use*graph_api](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/azuread/#force-fetching-groups-from-microsoft-graph-api) field.
        /// </summary>
        public InputMap<string> Custom
        {
            get => _custom ?? (_custom = new InputMap<string>());
            set => _custom = value;
        }

        /// <summary>
        /// Define allowed groups.
        /// </summary>
        [Input("defineAllowedGroups")]
        public Input<bool>? DefineAllowedGroups { get; set; }

        /// <summary>
        /// Define allowed teams ids.
        /// </summary>
        [Input("defineAllowedTeamsIds")]
        public Input<bool>? DefineAllowedTeamsIds { get; set; }

        /// <summary>
        /// Name of the key to use for user email lookup within the attributes map of OAuth2 ID token. Only applicable to Generic OAuth.
        /// </summary>
        [Input("emailAttributeName")]
        public Input<string>? EmailAttributeName { get; set; }

        /// <summary>
        /// JMESPath expression to use for user email lookup from the user information. Only applicable to Generic OAuth.
        /// </summary>
        [Input("emailAttributePath")]
        public Input<string>? EmailAttributePath { get; set; }

        /// <summary>
        /// If enabled, no scopes will be sent to the OAuth2 provider.
        /// </summary>
        [Input("emptyScopes")]
        public Input<bool>? EmptyScopes { get; set; }

        /// <summary>
        /// Define whether this configuration is enabled for the specified provider. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// JMESPath expression to use for user group lookup. If you configure allowed*groups, you must also configure groups*attribute_path.
        /// </summary>
        [Input("groupsAttributePath")]
        public Input<string>? GroupsAttributePath { get; set; }

        /// <summary>
        /// The name of the key used to extract the ID token from the returned OAuth2 token. Only applicable to Generic OAuth.
        /// </summary>
        [Input("idTokenAttributeName")]
        public Input<string>? IdTokenAttributeName { get; set; }

        /// <summary>
        /// JMESPath expression to use for user login lookup from the user ID token. Only applicable to Generic OAuth.
        /// </summary>
        [Input("loginAttributePath")]
        public Input<string>? LoginAttributePath { get; set; }

        /// <summary>
        /// Helpful if you use more than one identity providers or SSO protocols.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// JMESPath expression to use for user name lookup from the user ID token. This name will be used as the user’s display name. Only applicable to Generic OAuth.
        /// </summary>
        [Input("nameAttributePath")]
        public Input<string>? NameAttributePath { get; set; }

        /// <summary>
        /// JMESPath expression to use for Grafana role lookup.
        /// </summary>
        [Input("roleAttributePath")]
        public Input<string>? RoleAttributePath { get; set; }

        /// <summary>
        /// If enabled, denies user login if the Grafana role cannot be extracted using Role attribute path.
        /// </summary>
        [Input("roleAttributeStrict")]
        public Input<bool>? RoleAttributeStrict { get; set; }

        /// <summary>
        /// List of comma- or space-separated OAuth2 scopes.
        /// </summary>
        [Input("scopes")]
        public Input<string>? Scopes { get; set; }

        /// <summary>
        /// The URL to redirect the user to after signing out from Grafana.
        /// </summary>
        [Input("signoutRedirectUrl")]
        public Input<string>? SignoutRedirectUrl { get; set; }

        /// <summary>
        /// Prevent synchronizing users’ organization roles from your IdP.
        /// </summary>
        [Input("skipOrgRoleSync")]
        public Input<bool>? SkipOrgRoleSync { get; set; }

        /// <summary>
        /// String list of Team Ids. If set, the user must be a member of one of the given teams to log in. If you configure team*ids, you must also configure teams*url and team*ids*attribute_path.
        /// </summary>
        [Input("teamIds")]
        public Input<string>? TeamIds { get; set; }

        /// <summary>
        /// The JMESPath expression to use for Grafana Team Id lookup within the results returned by the teams_url endpoint. Only applicable to Generic OAuth.
        /// </summary>
        [Input("teamIdsAttributePath")]
        public Input<string>? TeamIdsAttributePath { get; set; }

        /// <summary>
        /// The URL used to query for Team Ids. If not set, the default value is /teams. If you configure teams*url, you must also configure team*ids*attribute*path. Only applicable to Generic OAuth.
        /// </summary>
        [Input("teamsUrl")]
        public Input<string>? TeamsUrl { get; set; }

        /// <summary>
        /// The path to the trusted certificate authority list. Is not applicable on Grafana Cloud.
        /// </summary>
        [Input("tlsClientCa")]
        public Input<string>? TlsClientCa { get; set; }

        /// <summary>
        /// The path to the certificate. Is not applicable on Grafana Cloud.
        /// </summary>
        [Input("tlsClientCert")]
        public Input<string>? TlsClientCert { get; set; }

        /// <summary>
        /// The path to the key. Is not applicable on Grafana Cloud.
        /// </summary>
        [Input("tlsClientKey")]
        public Input<string>? TlsClientKey { get; set; }

        /// <summary>
        /// If enabled, the client accepts any certificate presented by the server and any host name in that certificate. You should only use this for testing, because this mode leaves SSL/TLS susceptible to man-in-the-middle attacks.
        /// </summary>
        [Input("tlsSkipVerifyInsecure")]
        public Input<bool>? TlsSkipVerifyInsecure { get; set; }

        /// <summary>
        /// The token endpoint of your OAuth2 provider. Required for azuread, okta and generic_oauth providers.
        /// </summary>
        [Input("tokenUrl")]
        public Input<string>? TokenUrl { get; set; }

        /// <summary>
        /// If enabled, Grafana will use Proof Key for Code Exchange (PKCE) with the OAuth2 Authorization Code Grant.
        /// </summary>
        [Input("usePkce")]
        public Input<bool>? UsePkce { get; set; }

        /// <summary>
        /// If enabled, Grafana will fetch a new access token using the refresh token provided by the OAuth2 provider.
        /// </summary>
        [Input("useRefreshToken")]
        public Input<bool>? UseRefreshToken { get; set; }

        public SsoSettingsOauth2SettingsGetArgs()
        {
        }
        public static new SsoSettingsOauth2SettingsGetArgs Empty => new SsoSettingsOauth2SettingsGetArgs();
    }
}