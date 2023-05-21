// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana
{
    /// <summary>
    /// A job defines the queries and model parameters for a machine learning task.
    /// </summary>
    [GrafanaResourceType("grafana:index/machineLearningJob:MachineLearningJob")]
    public partial class MachineLearningJob : global::Pulumi.CustomResource
    {
        /// <summary>
        /// An object representing the custom labels added on the forecast.
        /// </summary>
        [Output("customLabels")]
        public Output<ImmutableDictionary<string, object>?> CustomLabels { get; private set; } = null!;

        /// <summary>
        /// The id of the datasource to query.
        /// </summary>
        [Output("datasourceId")]
        public Output<int?> DatasourceId { get; private set; } = null!;

        /// <summary>
        /// The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
        /// </summary>
        [Output("datasourceType")]
        public Output<string> DatasourceType { get; private set; } = null!;

        /// <summary>
        /// The uid of the datasource to query.
        /// </summary>
        [Output("datasourceUid")]
        public Output<string?> DatasourceUid { get; private set; } = null!;

        /// <summary>
        /// A description of the job.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A list of holiday IDs or names to take into account when training the model.
        /// </summary>
        [Output("holidays")]
        public Output<ImmutableArray<string>> Holidays { get; private set; } = null!;

        /// <summary>
        /// The hyperparameters used to fine tune the algorithm. See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to `map[]`.
        /// </summary>
        [Output("hyperParams")]
        public Output<ImmutableDictionary<string, object>?> HyperParams { get; private set; } = null!;

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `300`.
        /// </summary>
        [Output("interval")]
        public Output<int?> Interval { get; private set; } = null!;

        /// <summary>
        /// The metric used to query the job results.
        /// </summary>
        [Output("metric")]
        public Output<string> Metric { get; private set; } = null!;

        /// <summary>
        /// The name of the job.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// An object representing the query params to query Grafana with.
        /// </summary>
        [Output("queryParams")]
        public Output<ImmutableDictionary<string, object>> QueryParams { get; private set; } = null!;

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `7776000`.
        /// </summary>
        [Output("trainingWindow")]
        public Output<int?> TrainingWindow { get; private set; } = null!;


        /// <summary>
        /// Create a MachineLearningJob resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MachineLearningJob(string name, MachineLearningJobArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/machineLearningJob:MachineLearningJob", name, args ?? new MachineLearningJobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MachineLearningJob(string name, Input<string> id, MachineLearningJobState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/machineLearningJob:MachineLearningJob", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/lbrlabs",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing MachineLearningJob resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MachineLearningJob Get(string name, Input<string> id, MachineLearningJobState? state = null, CustomResourceOptions? options = null)
        {
            return new MachineLearningJob(name, id, state, options);
        }
    }

    public sealed class MachineLearningJobArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLabels")]
        private InputMap<object>? _customLabels;

        /// <summary>
        /// An object representing the custom labels added on the forecast.
        /// </summary>
        public InputMap<object> CustomLabels
        {
            get => _customLabels ?? (_customLabels = new InputMap<object>());
            set => _customLabels = value;
        }

        /// <summary>
        /// The id of the datasource to query.
        /// </summary>
        [Input("datasourceId")]
        public Input<int>? DatasourceId { get; set; }

        /// <summary>
        /// The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
        /// </summary>
        [Input("datasourceType", required: true)]
        public Input<string> DatasourceType { get; set; } = null!;

        /// <summary>
        /// The uid of the datasource to query.
        /// </summary>
        [Input("datasourceUid")]
        public Input<string>? DatasourceUid { get; set; }

        /// <summary>
        /// A description of the job.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("holidays")]
        private InputList<string>? _holidays;

        /// <summary>
        /// A list of holiday IDs or names to take into account when training the model.
        /// </summary>
        public InputList<string> Holidays
        {
            get => _holidays ?? (_holidays = new InputList<string>());
            set => _holidays = value;
        }

        [Input("hyperParams")]
        private InputMap<object>? _hyperParams;

        /// <summary>
        /// The hyperparameters used to fine tune the algorithm. See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to `map[]`.
        /// </summary>
        public InputMap<object> HyperParams
        {
            get => _hyperParams ?? (_hyperParams = new InputMap<object>());
            set => _hyperParams = value;
        }

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `300`.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// The metric used to query the job results.
        /// </summary>
        [Input("metric", required: true)]
        public Input<string> Metric { get; set; } = null!;

        /// <summary>
        /// The name of the job.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("queryParams", required: true)]
        private InputMap<object>? _queryParams;

        /// <summary>
        /// An object representing the query params to query Grafana with.
        /// </summary>
        public InputMap<object> QueryParams
        {
            get => _queryParams ?? (_queryParams = new InputMap<object>());
            set => _queryParams = value;
        }

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `7776000`.
        /// </summary>
        [Input("trainingWindow")]
        public Input<int>? TrainingWindow { get; set; }

        public MachineLearningJobArgs()
        {
        }
        public static new MachineLearningJobArgs Empty => new MachineLearningJobArgs();
    }

    public sealed class MachineLearningJobState : global::Pulumi.ResourceArgs
    {
        [Input("customLabels")]
        private InputMap<object>? _customLabels;

        /// <summary>
        /// An object representing the custom labels added on the forecast.
        /// </summary>
        public InputMap<object> CustomLabels
        {
            get => _customLabels ?? (_customLabels = new InputMap<object>());
            set => _customLabels = value;
        }

        /// <summary>
        /// The id of the datasource to query.
        /// </summary>
        [Input("datasourceId")]
        public Input<int>? DatasourceId { get; set; }

        /// <summary>
        /// The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
        /// </summary>
        [Input("datasourceType")]
        public Input<string>? DatasourceType { get; set; }

        /// <summary>
        /// The uid of the datasource to query.
        /// </summary>
        [Input("datasourceUid")]
        public Input<string>? DatasourceUid { get; set; }

        /// <summary>
        /// A description of the job.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("holidays")]
        private InputList<string>? _holidays;

        /// <summary>
        /// A list of holiday IDs or names to take into account when training the model.
        /// </summary>
        public InputList<string> Holidays
        {
            get => _holidays ?? (_holidays = new InputList<string>());
            set => _holidays = value;
        }

        [Input("hyperParams")]
        private InputMap<object>? _hyperParams;

        /// <summary>
        /// The hyperparameters used to fine tune the algorithm. See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to `map[]`.
        /// </summary>
        public InputMap<object> HyperParams
        {
            get => _hyperParams ?? (_hyperParams = new InputMap<object>());
            set => _hyperParams = value;
        }

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `300`.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// The metric used to query the job results.
        /// </summary>
        [Input("metric")]
        public Input<string>? Metric { get; set; }

        /// <summary>
        /// The name of the job.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("queryParams")]
        private InputMap<object>? _queryParams;

        /// <summary>
        /// An object representing the query params to query Grafana with.
        /// </summary>
        public InputMap<object> QueryParams
        {
            get => _queryParams ?? (_queryParams = new InputMap<object>());
            set => _queryParams = value;
        }

        /// <summary>
        /// The data interval in seconds to train the data on. Defaults to `7776000`.
        /// </summary>
        [Input("trainingWindow")]
        public Input<int>? TrainingWindow { get; set; }

        public MachineLearningJobState()
        {
        }
        public static new MachineLearningJobState Empty => new MachineLearningJobState();
    }
}
