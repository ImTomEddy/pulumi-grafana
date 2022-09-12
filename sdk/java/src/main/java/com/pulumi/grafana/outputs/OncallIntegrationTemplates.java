// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.grafana.outputs.OncallIntegrationTemplatesSlack;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class OncallIntegrationTemplates {
    /**
     * @return Template for the key by which alerts are grouped.
     * 
     */
    private @Nullable String groupingKey;
    /**
     * @return Template for sending a signal to resolve the Incident.
     * 
     */
    private @Nullable String resolveSignal;
    /**
     * @return Templates for Slack.
     * 
     */
    private @Nullable OncallIntegrationTemplatesSlack slack;

    private OncallIntegrationTemplates() {}
    /**
     * @return Template for the key by which alerts are grouped.
     * 
     */
    public Optional<String> groupingKey() {
        return Optional.ofNullable(this.groupingKey);
    }
    /**
     * @return Template for sending a signal to resolve the Incident.
     * 
     */
    public Optional<String> resolveSignal() {
        return Optional.ofNullable(this.resolveSignal);
    }
    /**
     * @return Templates for Slack.
     * 
     */
    public Optional<OncallIntegrationTemplatesSlack> slack() {
        return Optional.ofNullable(this.slack);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(OncallIntegrationTemplates defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String groupingKey;
        private @Nullable String resolveSignal;
        private @Nullable OncallIntegrationTemplatesSlack slack;
        public Builder() {}
        public Builder(OncallIntegrationTemplates defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.groupingKey = defaults.groupingKey;
    	      this.resolveSignal = defaults.resolveSignal;
    	      this.slack = defaults.slack;
        }

        @CustomType.Setter
        public Builder groupingKey(@Nullable String groupingKey) {
            this.groupingKey = groupingKey;
            return this;
        }
        @CustomType.Setter
        public Builder resolveSignal(@Nullable String resolveSignal) {
            this.resolveSignal = resolveSignal;
            return this;
        }
        @CustomType.Setter
        public Builder slack(@Nullable OncallIntegrationTemplatesSlack slack) {
            this.slack = slack;
            return this;
        }
        public OncallIntegrationTemplates build() {
            final var o = new OncallIntegrationTemplates();
            o.groupingKey = groupingKey;
            o.resolveSignal = resolveSignal;
            o.slack = slack;
            return o;
        }
    }
}