// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Inputs
{

    public sealed class ContactPointOpsgenyResponderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the responder. Must be specified if name and username are empty.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of the responder. Must be specified if username and id are empty.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Type of the responder. Supported: team, teams, user, escalation, schedule or a template that is expanded to one of these values.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// The user name to use when making a call to the Kafka REST Proxy
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ContactPointOpsgenyResponderArgs()
        {
        }
        public static new ContactPointOpsgenyResponderArgs Empty => new ContactPointOpsgenyResponderArgs();
    }
}
