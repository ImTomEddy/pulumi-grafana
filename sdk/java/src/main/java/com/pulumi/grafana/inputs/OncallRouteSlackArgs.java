// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class OncallRouteSlackArgs extends com.pulumi.resources.ResourceArgs {

    public static final OncallRouteSlackArgs Empty = new OncallRouteSlackArgs();

    /**
     * Slack channel id. Alerts will be directed to this channel in Slack.
     * 
     */
    @Import(name="channelId")
    private @Nullable Output<String> channelId;

    /**
     * @return Slack channel id. Alerts will be directed to this channel in Slack.
     * 
     */
    public Optional<Output<String>> channelId() {
        return Optional.ofNullable(this.channelId);
    }

    /**
     * Enable notification in Slack. Defaults to `true`.
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return Enable notification in Slack. Defaults to `true`.
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    private OncallRouteSlackArgs() {}

    private OncallRouteSlackArgs(OncallRouteSlackArgs $) {
        this.channelId = $.channelId;
        this.enabled = $.enabled;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(OncallRouteSlackArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private OncallRouteSlackArgs $;

        public Builder() {
            $ = new OncallRouteSlackArgs();
        }

        public Builder(OncallRouteSlackArgs defaults) {
            $ = new OncallRouteSlackArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param channelId Slack channel id. Alerts will be directed to this channel in Slack.
         * 
         * @return builder
         * 
         */
        public Builder channelId(@Nullable Output<String> channelId) {
            $.channelId = channelId;
            return this;
        }

        /**
         * @param channelId Slack channel id. Alerts will be directed to this channel in Slack.
         * 
         * @return builder
         * 
         */
        public Builder channelId(String channelId) {
            return channelId(Output.of(channelId));
        }

        /**
         * @param enabled Enable notification in Slack. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled Enable notification in Slack. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        public OncallRouteSlackArgs build() {
            return $;
        }
    }

}