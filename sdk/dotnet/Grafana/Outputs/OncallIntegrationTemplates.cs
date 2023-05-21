// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Outputs
{

    [OutputType]
    public sealed class OncallIntegrationTemplates
    {
        /// <summary>
        /// Template for sending a signal to acknowledge the Incident.
        /// </summary>
        public readonly string? AcknowledgeSignal;
        /// <summary>
        /// Templates for Email.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesEmail? Email;
        /// <summary>
        /// Template for the key by which alerts are grouped.
        /// </summary>
        public readonly string? GroupingKey;
        /// <summary>
        /// Templates for Microsoft Teams.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesMicrosoftTeams? MicrosoftTeams;
        /// <summary>
        /// Templates for Phone Call.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesPhoneCall? PhoneCall;
        /// <summary>
        /// Template for sending a signal to resolve the Incident.
        /// </summary>
        public readonly string? ResolveSignal;
        /// <summary>
        /// Templates for Slack.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesSlack? Slack;
        /// <summary>
        /// Templates for SMS.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesSms? Sms;
        /// <summary>
        /// Template for a source link.
        /// </summary>
        public readonly string? SourceLink;
        /// <summary>
        /// Templates for Telegram.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesTelegram? Telegram;
        /// <summary>
        /// Templates for Web.
        /// </summary>
        public readonly Outputs.OncallIntegrationTemplatesWeb? Web;

        [OutputConstructor]
        private OncallIntegrationTemplates(
            string? acknowledgeSignal,

            Outputs.OncallIntegrationTemplatesEmail? email,

            string? groupingKey,

            Outputs.OncallIntegrationTemplatesMicrosoftTeams? microsoftTeams,

            Outputs.OncallIntegrationTemplatesPhoneCall? phoneCall,

            string? resolveSignal,

            Outputs.OncallIntegrationTemplatesSlack? slack,

            Outputs.OncallIntegrationTemplatesSms? sms,

            string? sourceLink,

            Outputs.OncallIntegrationTemplatesTelegram? telegram,

            Outputs.OncallIntegrationTemplatesWeb? web)
        {
            AcknowledgeSignal = acknowledgeSignal;
            Email = email;
            GroupingKey = groupingKey;
            MicrosoftTeams = microsoftTeams;
            PhoneCall = phoneCall;
            ResolveSignal = resolveSignal;
            Slack = slack;
            Sms = sms;
            SourceLink = sourceLink;
            Telegram = telegram;
            Web = web;
        }
    }
}
