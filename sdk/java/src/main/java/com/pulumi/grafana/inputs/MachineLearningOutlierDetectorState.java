// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.MachineLearningOutlierDetectorAlgorithmArgs;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MachineLearningOutlierDetectorState extends com.pulumi.resources.ResourceArgs {

    public static final MachineLearningOutlierDetectorState Empty = new MachineLearningOutlierDetectorState();

    /**
     * The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
     * 
     */
    @Import(name="algorithm")
    private @Nullable Output<MachineLearningOutlierDetectorAlgorithmArgs> algorithm;

    /**
     * @return The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
     * 
     */
    public Optional<Output<MachineLearningOutlierDetectorAlgorithmArgs>> algorithm() {
        return Optional.ofNullable(this.algorithm);
    }

    /**
     * The id of the datasource to query.
     * 
     */
    @Import(name="datasourceId")
    private @Nullable Output<Integer> datasourceId;

    /**
     * @return The id of the datasource to query.
     * 
     */
    public Optional<Output<Integer>> datasourceId() {
        return Optional.ofNullable(this.datasourceId);
    }

    /**
     * The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
     * 
     */
    @Import(name="datasourceType")
    private @Nullable Output<String> datasourceType;

    /**
     * @return The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
     * 
     */
    public Optional<Output<String>> datasourceType() {
        return Optional.ofNullable(this.datasourceType);
    }

    /**
     * The uid of the datasource to query.
     * 
     */
    @Import(name="datasourceUid")
    private @Nullable Output<String> datasourceUid;

    /**
     * @return The uid of the datasource to query.
     * 
     */
    public Optional<Output<String>> datasourceUid() {
        return Optional.ofNullable(this.datasourceUid);
    }

    /**
     * A description of the outlier detector.
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return A description of the outlier detector.
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * The data interval in seconds to monitor. Defaults to `300`.
     * 
     */
    @Import(name="interval")
    private @Nullable Output<Integer> interval;

    /**
     * @return The data interval in seconds to monitor. Defaults to `300`.
     * 
     */
    public Optional<Output<Integer>> interval() {
        return Optional.ofNullable(this.interval);
    }

    /**
     * The metric used to query the outlier detector results.
     * 
     */
    @Import(name="metric")
    private @Nullable Output<String> metric;

    /**
     * @return The metric used to query the outlier detector results.
     * 
     */
    public Optional<Output<String>> metric() {
        return Optional.ofNullable(this.metric);
    }

    /**
     * The name of the outlier detector.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the outlier detector.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * An object representing the query params to query Grafana with.
     * 
     */
    @Import(name="queryParams")
    private @Nullable Output<Map<String,Object>> queryParams;

    /**
     * @return An object representing the query params to query Grafana with.
     * 
     */
    public Optional<Output<Map<String,Object>>> queryParams() {
        return Optional.ofNullable(this.queryParams);
    }

    private MachineLearningOutlierDetectorState() {}

    private MachineLearningOutlierDetectorState(MachineLearningOutlierDetectorState $) {
        this.algorithm = $.algorithm;
        this.datasourceId = $.datasourceId;
        this.datasourceType = $.datasourceType;
        this.datasourceUid = $.datasourceUid;
        this.description = $.description;
        this.interval = $.interval;
        this.metric = $.metric;
        this.name = $.name;
        this.queryParams = $.queryParams;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MachineLearningOutlierDetectorState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MachineLearningOutlierDetectorState $;

        public Builder() {
            $ = new MachineLearningOutlierDetectorState();
        }

        public Builder(MachineLearningOutlierDetectorState defaults) {
            $ = new MachineLearningOutlierDetectorState(Objects.requireNonNull(defaults));
        }

        /**
         * @param algorithm The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(@Nullable Output<MachineLearningOutlierDetectorAlgorithmArgs> algorithm) {
            $.algorithm = algorithm;
            return this;
        }

        /**
         * @param algorithm The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(MachineLearningOutlierDetectorAlgorithmArgs algorithm) {
            return algorithm(Output.of(algorithm));
        }

        /**
         * @param datasourceId The id of the datasource to query.
         * 
         * @return builder
         * 
         */
        public Builder datasourceId(@Nullable Output<Integer> datasourceId) {
            $.datasourceId = datasourceId;
            return this;
        }

        /**
         * @param datasourceId The id of the datasource to query.
         * 
         * @return builder
         * 
         */
        public Builder datasourceId(Integer datasourceId) {
            return datasourceId(Output.of(datasourceId));
        }

        /**
         * @param datasourceType The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
         * 
         * @return builder
         * 
         */
        public Builder datasourceType(@Nullable Output<String> datasourceType) {
            $.datasourceType = datasourceType;
            return this;
        }

        /**
         * @param datasourceType The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
         * 
         * @return builder
         * 
         */
        public Builder datasourceType(String datasourceType) {
            return datasourceType(Output.of(datasourceType));
        }

        /**
         * @param datasourceUid The uid of the datasource to query.
         * 
         * @return builder
         * 
         */
        public Builder datasourceUid(@Nullable Output<String> datasourceUid) {
            $.datasourceUid = datasourceUid;
            return this;
        }

        /**
         * @param datasourceUid The uid of the datasource to query.
         * 
         * @return builder
         * 
         */
        public Builder datasourceUid(String datasourceUid) {
            return datasourceUid(Output.of(datasourceUid));
        }

        /**
         * @param description A description of the outlier detector.
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description A description of the outlier detector.
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param interval The data interval in seconds to monitor. Defaults to `300`.
         * 
         * @return builder
         * 
         */
        public Builder interval(@Nullable Output<Integer> interval) {
            $.interval = interval;
            return this;
        }

        /**
         * @param interval The data interval in seconds to monitor. Defaults to `300`.
         * 
         * @return builder
         * 
         */
        public Builder interval(Integer interval) {
            return interval(Output.of(interval));
        }

        /**
         * @param metric The metric used to query the outlier detector results.
         * 
         * @return builder
         * 
         */
        public Builder metric(@Nullable Output<String> metric) {
            $.metric = metric;
            return this;
        }

        /**
         * @param metric The metric used to query the outlier detector results.
         * 
         * @return builder
         * 
         */
        public Builder metric(String metric) {
            return metric(Output.of(metric));
        }

        /**
         * @param name The name of the outlier detector.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the outlier detector.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param queryParams An object representing the query params to query Grafana with.
         * 
         * @return builder
         * 
         */
        public Builder queryParams(@Nullable Output<Map<String,Object>> queryParams) {
            $.queryParams = queryParams;
            return this;
        }

        /**
         * @param queryParams An object representing the query params to query Grafana with.
         * 
         * @return builder
         * 
         */
        public Builder queryParams(Map<String,Object> queryParams) {
            return queryParams(Output.of(queryParams));
        }

        public MachineLearningOutlierDetectorState build() {
            return $;
        }
    }

}