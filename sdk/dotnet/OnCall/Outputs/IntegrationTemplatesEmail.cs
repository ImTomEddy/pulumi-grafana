// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.OnCall.Outputs
{

    [OutputType]
    public sealed class IntegrationTemplatesEmail
    {
        /// <summary>
        /// Template for Alert message.
        /// </summary>
        public readonly string? Message;
        /// <summary>
        /// Template for Alert title.
        /// </summary>
        public readonly string? Title;

        [OutputConstructor]
        private IntegrationTemplatesEmail(
            string? message,

            string? title)
        {
            Message = message;
            Title = title;
        }
    }
}
