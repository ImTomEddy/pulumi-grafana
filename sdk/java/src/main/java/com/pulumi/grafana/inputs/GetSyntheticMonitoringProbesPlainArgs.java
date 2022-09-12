// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetSyntheticMonitoringProbesPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetSyntheticMonitoringProbesPlainArgs Empty = new GetSyntheticMonitoringProbesPlainArgs();

    /**
     * If true, only probes that are not deprecated will be returned. Defaults to `true`.
     * 
     */
    @Import(name="filterDeprecated")
    private @Nullable Boolean filterDeprecated;

    /**
     * @return If true, only probes that are not deprecated will be returned. Defaults to `true`.
     * 
     */
    public Optional<Boolean> filterDeprecated() {
        return Optional.ofNullable(this.filterDeprecated);
    }

    private GetSyntheticMonitoringProbesPlainArgs() {}

    private GetSyntheticMonitoringProbesPlainArgs(GetSyntheticMonitoringProbesPlainArgs $) {
        this.filterDeprecated = $.filterDeprecated;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetSyntheticMonitoringProbesPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetSyntheticMonitoringProbesPlainArgs $;

        public Builder() {
            $ = new GetSyntheticMonitoringProbesPlainArgs();
        }

        public Builder(GetSyntheticMonitoringProbesPlainArgs defaults) {
            $ = new GetSyntheticMonitoringProbesPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param filterDeprecated If true, only probes that are not deprecated will be returned. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder filterDeprecated(@Nullable Boolean filterDeprecated) {
            $.filterDeprecated = filterDeprecated;
            return this;
        }

        public GetSyntheticMonitoringProbesPlainArgs build() {
            return $;
        }
    }

}