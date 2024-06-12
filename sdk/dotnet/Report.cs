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
    /// <summary>
    /// **Note:** This resource is available only with Grafana Enterprise 7.+.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/create-reports/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/reporting/)
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var testDashboard = new Grafana.Dashboard("testDashboard", new()
    ///     {
    ///         ConfigJson = @"{
    ///   ""uid"": ""report-dashboard"",
    ///   ""title"": ""report-dashboard""
    /// }
    /// ",
    ///         Message = "inital commit.",
    ///     });
    /// 
    ///     var testReport = new Grafana.Report("testReport", new()
    ///     {
    ///         DashboardUid = testDashboard.Uid,
    ///         Recipients = new[]
    ///         {
    ///             "some@email.com",
    ///         },
    ///         Schedule = new Grafana.Inputs.ReportScheduleArgs
    ///         {
    ///             Frequency = "hourly",
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:index/report:Report name "{{ id }}"
    /// ```
    /// 
    /// ```sh
    /// $ pulumi import grafana:index/report:Report name "{{ orgID }}:{{ id }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/report:Report")]
    public partial class Report : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        /// </summary>
        [Output("dashboardId")]
        public Output<int> DashboardId { get; private set; } = null!;

        /// <summary>
        /// Dashboard to be sent in the report.
        /// </summary>
        [Output("dashboardUid")]
        public Output<string> DashboardUid { get; private set; } = null!;

        /// <summary>
        /// List of dashboards to render into the report
        /// </summary>
        [Output("dashboards")]
        public Output<ImmutableArray<Outputs.ReportDashboard>> Dashboards { get; private set; } = null!;

        /// <summary>
        /// Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        /// </summary>
        [Output("formats")]
        public Output<ImmutableArray<string>> Formats { get; private set; } = null!;

        /// <summary>
        /// Whether to include a link to the dashboard in the report. Defaults to `true`.
        /// </summary>
        [Output("includeDashboardLink")]
        public Output<bool?> IncludeDashboardLink { get; private set; } = null!;

        /// <summary>
        /// Whether to include a CSV file of table panel data. Defaults to `false`.
        /// </summary>
        [Output("includeTableCsv")]
        public Output<bool?> IncludeTableCsv { get; private set; } = null!;

        /// <summary>
        /// Layout of the report. Allowed values: `simple`, `grid`. Defaults to `grid`.
        /// </summary>
        [Output("layout")]
        public Output<string?> Layout { get; private set; } = null!;

        /// <summary>
        /// Message to be sent in the report.
        /// </summary>
        [Output("message")]
        public Output<string?> Message { get; private set; } = null!;

        /// <summary>
        /// Name of the report.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// Orientation of the report. Allowed values: `landscape`, `portrait`. Defaults to `landscape`.
        /// </summary>
        [Output("orientation")]
        public Output<string?> Orientation { get; private set; } = null!;

        /// <summary>
        /// List of recipients of the report.
        /// </summary>
        [Output("recipients")]
        public Output<ImmutableArray<string>> Recipients { get; private set; } = null!;

        /// <summary>
        /// Reply-to email address of the report.
        /// </summary>
        [Output("replyTo")]
        public Output<string?> ReplyTo { get; private set; } = null!;

        /// <summary>
        /// Schedule of the report.
        /// </summary>
        [Output("schedule")]
        public Output<Outputs.ReportSchedule> Schedule { get; private set; } = null!;

        /// <summary>
        /// Time range of the report.
        /// </summary>
        [Output("timeRange")]
        public Output<Outputs.ReportTimeRange?> TimeRange { get; private set; } = null!;


        /// <summary>
        /// Create a Report resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Report(string name, ReportArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/report:Report", name, args ?? new ReportArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Report(string name, Input<string> id, ReportState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/report:Report", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Report resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Report Get(string name, Input<string> id, ReportState? state = null, CustomResourceOptions? options = null)
        {
            return new Report(name, id, state, options);
        }
    }

    public sealed class ReportArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        /// </summary>
        [Input("dashboardId")]
        public Input<int>? DashboardId { get; set; }

        /// <summary>
        /// Dashboard to be sent in the report.
        /// </summary>
        [Input("dashboardUid")]
        public Input<string>? DashboardUid { get; set; }

        [Input("dashboards")]
        private InputList<Inputs.ReportDashboardArgs>? _dashboards;

        /// <summary>
        /// List of dashboards to render into the report
        /// </summary>
        public InputList<Inputs.ReportDashboardArgs> Dashboards
        {
            get => _dashboards ?? (_dashboards = new InputList<Inputs.ReportDashboardArgs>());
            set => _dashboards = value;
        }

        [Input("formats")]
        private InputList<string>? _formats;

        /// <summary>
        /// Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        /// </summary>
        public InputList<string> Formats
        {
            get => _formats ?? (_formats = new InputList<string>());
            set => _formats = value;
        }

        /// <summary>
        /// Whether to include a link to the dashboard in the report. Defaults to `true`.
        /// </summary>
        [Input("includeDashboardLink")]
        public Input<bool>? IncludeDashboardLink { get; set; }

        /// <summary>
        /// Whether to include a CSV file of table panel data. Defaults to `false`.
        /// </summary>
        [Input("includeTableCsv")]
        public Input<bool>? IncludeTableCsv { get; set; }

        /// <summary>
        /// Layout of the report. Allowed values: `simple`, `grid`. Defaults to `grid`.
        /// </summary>
        [Input("layout")]
        public Input<string>? Layout { get; set; }

        /// <summary>
        /// Message to be sent in the report.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// Name of the report.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// Orientation of the report. Allowed values: `landscape`, `portrait`. Defaults to `landscape`.
        /// </summary>
        [Input("orientation")]
        public Input<string>? Orientation { get; set; }

        [Input("recipients", required: true)]
        private InputList<string>? _recipients;

        /// <summary>
        /// List of recipients of the report.
        /// </summary>
        public InputList<string> Recipients
        {
            get => _recipients ?? (_recipients = new InputList<string>());
            set => _recipients = value;
        }

        /// <summary>
        /// Reply-to email address of the report.
        /// </summary>
        [Input("replyTo")]
        public Input<string>? ReplyTo { get; set; }

        /// <summary>
        /// Schedule of the report.
        /// </summary>
        [Input("schedule", required: true)]
        public Input<Inputs.ReportScheduleArgs> Schedule { get; set; } = null!;

        /// <summary>
        /// Time range of the report.
        /// </summary>
        [Input("timeRange")]
        public Input<Inputs.ReportTimeRangeArgs>? TimeRange { get; set; }

        public ReportArgs()
        {
        }
        public static new ReportArgs Empty => new ReportArgs();
    }

    public sealed class ReportState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
        /// </summary>
        [Input("dashboardId")]
        public Input<int>? DashboardId { get; set; }

        /// <summary>
        /// Dashboard to be sent in the report.
        /// </summary>
        [Input("dashboardUid")]
        public Input<string>? DashboardUid { get; set; }

        [Input("dashboards")]
        private InputList<Inputs.ReportDashboardGetArgs>? _dashboards;

        /// <summary>
        /// List of dashboards to render into the report
        /// </summary>
        public InputList<Inputs.ReportDashboardGetArgs> Dashboards
        {
            get => _dashboards ?? (_dashboards = new InputList<Inputs.ReportDashboardGetArgs>());
            set => _dashboards = value;
        }

        [Input("formats")]
        private InputList<string>? _formats;

        /// <summary>
        /// Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
        /// </summary>
        public InputList<string> Formats
        {
            get => _formats ?? (_formats = new InputList<string>());
            set => _formats = value;
        }

        /// <summary>
        /// Whether to include a link to the dashboard in the report. Defaults to `true`.
        /// </summary>
        [Input("includeDashboardLink")]
        public Input<bool>? IncludeDashboardLink { get; set; }

        /// <summary>
        /// Whether to include a CSV file of table panel data. Defaults to `false`.
        /// </summary>
        [Input("includeTableCsv")]
        public Input<bool>? IncludeTableCsv { get; set; }

        /// <summary>
        /// Layout of the report. Allowed values: `simple`, `grid`. Defaults to `grid`.
        /// </summary>
        [Input("layout")]
        public Input<string>? Layout { get; set; }

        /// <summary>
        /// Message to be sent in the report.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// Name of the report.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// Orientation of the report. Allowed values: `landscape`, `portrait`. Defaults to `landscape`.
        /// </summary>
        [Input("orientation")]
        public Input<string>? Orientation { get; set; }

        [Input("recipients")]
        private InputList<string>? _recipients;

        /// <summary>
        /// List of recipients of the report.
        /// </summary>
        public InputList<string> Recipients
        {
            get => _recipients ?? (_recipients = new InputList<string>());
            set => _recipients = value;
        }

        /// <summary>
        /// Reply-to email address of the report.
        /// </summary>
        [Input("replyTo")]
        public Input<string>? ReplyTo { get; set; }

        /// <summary>
        /// Schedule of the report.
        /// </summary>
        [Input("schedule")]
        public Input<Inputs.ReportScheduleGetArgs>? Schedule { get; set; }

        /// <summary>
        /// Time range of the report.
        /// </summary>
        [Input("timeRange")]
        public Input<Inputs.ReportTimeRangeGetArgs>? TimeRange { get; set; }

        public ReportState()
        {
        }
        public static new ReportState Empty => new ReportState();
    }
}
