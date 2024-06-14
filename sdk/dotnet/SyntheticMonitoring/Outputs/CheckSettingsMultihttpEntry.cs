// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring.Outputs
{

    [OutputType]
    public sealed class CheckSettingsMultihttpEntry
    {
        /// <summary>
        /// Assertions to make on the request response
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckSettingsMultihttpEntryAssertion> Assertions;
        /// <summary>
        /// An individual MultiHTTP request
        /// </summary>
        public readonly Outputs.CheckSettingsMultihttpEntryRequest? Request;
        /// <summary>
        /// Variables to extract from the request response
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckSettingsMultihttpEntryVariable> Variables;

        [OutputConstructor]
        private CheckSettingsMultihttpEntry(
            ImmutableArray<Outputs.CheckSettingsMultihttpEntryAssertion> assertions,

            Outputs.CheckSettingsMultihttpEntryRequest? request,

            ImmutableArray<Outputs.CheckSettingsMultihttpEntryVariable> variables)
        {
            Assertions = assertions;
            Request = request;
            Variables = variables;
        }
    }
}
