// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs_Pulumi.Grafana.Outputs
{

    [OutputType]
    public sealed class BuiltinRoleAssignmentRole
    {
        /// <summary>
        /// States whether the assignment is available across all organizations or not. Defaults to `false`.
        /// </summary>
        public readonly bool? Global;
        /// <summary>
        /// Unique identifier of the role to assign to `builtin_role`.
        /// </summary>
        public readonly string Uid;

        [OutputConstructor]
        private BuiltinRoleAssignmentRole(
            bool? global,

            string uid)
        {
            Global = global;
            Uid = uid;
        }
    }
}