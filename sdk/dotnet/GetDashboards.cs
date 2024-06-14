// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana
{
    [Obsolete(@"grafana.index/getdashboards.getDashboards has been deprecated in favor of grafana.oss/getdashboards.getDashboards")]
    public static class GetDashboards
    {
        public static Task<GetDashboardsResult> InvokeAsync(GetDashboardsArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDashboardsResult>("grafana:index/getDashboards:getDashboards", args ?? new GetDashboardsArgs(), options.WithDefaults());

        public static Output<GetDashboardsResult> Invoke(GetDashboardsInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDashboardsResult>("grafana:index/getDashboards:getDashboards", args ?? new GetDashboardsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDashboardsArgs : global::Pulumi.InvokeArgs
    {
        [Input("folderIds")]
        private List<int>? _folderIds;
        [Obsolete(@"Use `folder_uids` instead.")]
        public List<int> FolderIds
        {
            get => _folderIds ?? (_folderIds = new List<int>());
            set => _folderIds = value;
        }

        [Input("folderUids")]
        private List<string>? _folderUids;
        public List<string> FolderUids
        {
            get => _folderUids ?? (_folderUids = new List<string>());
            set => _folderUids = value;
        }

        [Input("limit")]
        public int? Limit { get; set; }

        [Input("orgId")]
        public string? OrgId { get; set; }

        [Input("tags")]
        private List<string>? _tags;
        public List<string> Tags
        {
            get => _tags ?? (_tags = new List<string>());
            set => _tags = value;
        }

        public GetDashboardsArgs()
        {
        }
        public static new GetDashboardsArgs Empty => new GetDashboardsArgs();
    }

    public sealed class GetDashboardsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("folderIds")]
        private InputList<int>? _folderIds;
        [Obsolete(@"Use `folder_uids` instead.")]
        public InputList<int> FolderIds
        {
            get => _folderIds ?? (_folderIds = new InputList<int>());
            set => _folderIds = value;
        }

        [Input("folderUids")]
        private InputList<string>? _folderUids;
        public InputList<string> FolderUids
        {
            get => _folderUids ?? (_folderUids = new InputList<string>());
            set => _folderUids = value;
        }

        [Input("limit")]
        public Input<int>? Limit { get; set; }

        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        public GetDashboardsInvokeArgs()
        {
        }
        public static new GetDashboardsInvokeArgs Empty => new GetDashboardsInvokeArgs();
    }


    [OutputType]
    public sealed class GetDashboardsResult
    {
        public readonly ImmutableArray<Outputs.GetDashboardsDashboardResult> Dashboards;
        public readonly ImmutableArray<int> FolderIds;
        public readonly ImmutableArray<string> FolderUids;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly int? Limit;
        public readonly string? OrgId;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetDashboardsResult(
            ImmutableArray<Outputs.GetDashboardsDashboardResult> dashboards,

            ImmutableArray<int> folderIds,

            ImmutableArray<string> folderUids,

            string id,

            int? limit,

            string? orgId,

            ImmutableArray<string> tags)
        {
            Dashboards = dashboards;
            FolderIds = folderIds;
            FolderUids = folderUids;
            Id = id;
            Limit = limit;
            OrgId = orgId;
            Tags = tags;
        }
    }
}
