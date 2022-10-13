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
    public sealed class ContactPointVictorop
    {
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        public readonly bool? DisableResolveMessage;
        /// <summary>
        /// The VictorOps alert state - typically either `CRITICAL` or `RECOVERY`.
        /// </summary>
        public readonly string? MessageType;
        /// <summary>
        /// Additional custom properties to attach to the notifier. Defaults to `map[]`.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Settings;
        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        public readonly string? Uid;
        /// <summary>
        /// The VictorOps webhook URL.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private ContactPointVictorop(
            bool? disableResolveMessage,

            string? messageType,

            ImmutableDictionary<string, string>? settings,

            string? uid,

            string url)
        {
            DisableResolveMessage = disableResolveMessage;
            MessageType = messageType;
            Settings = settings;
            Uid = uid;
            Url = url;
        }
    }
}