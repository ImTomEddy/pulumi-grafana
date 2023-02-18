// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Double;
import java.util.Objects;

@CustomType
public final class MachineLearningOutlierDetectorAlgorithmConfig {
    private Double epsilon;

    private MachineLearningOutlierDetectorAlgorithmConfig() {}
    public Double epsilon() {
        return this.epsilon;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(MachineLearningOutlierDetectorAlgorithmConfig defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Double epsilon;
        public Builder() {}
        public Builder(MachineLearningOutlierDetectorAlgorithmConfig defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.epsilon = defaults.epsilon;
        }

        @CustomType.Setter
        public Builder epsilon(Double epsilon) {
            this.epsilon = Objects.requireNonNull(epsilon);
            return this;
        }
        public MachineLearningOutlierDetectorAlgorithmConfig build() {
            final var o = new MachineLearningOutlierDetectorAlgorithmConfig();
            o.epsilon = epsilon;
            return o;
        }
    }
}