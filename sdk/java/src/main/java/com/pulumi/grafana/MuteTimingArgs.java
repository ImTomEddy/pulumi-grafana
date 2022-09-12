// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.MuteTimingIntervalArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MuteTimingArgs extends com.pulumi.resources.ResourceArgs {

    public static final MuteTimingArgs Empty = new MuteTimingArgs();

    /**
     * The time intervals at which to mute notifications.
     * 
     */
    @Import(name="intervals")
    private @Nullable Output<List<MuteTimingIntervalArgs>> intervals;

    /**
     * @return The time intervals at which to mute notifications.
     * 
     */
    public Optional<Output<List<MuteTimingIntervalArgs>>> intervals() {
        return Optional.ofNullable(this.intervals);
    }

    /**
     * The name of the mute timing.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the mute timing.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    private MuteTimingArgs() {}

    private MuteTimingArgs(MuteTimingArgs $) {
        this.intervals = $.intervals;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MuteTimingArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MuteTimingArgs $;

        public Builder() {
            $ = new MuteTimingArgs();
        }

        public Builder(MuteTimingArgs defaults) {
            $ = new MuteTimingArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param intervals The time intervals at which to mute notifications.
         * 
         * @return builder
         * 
         */
        public Builder intervals(@Nullable Output<List<MuteTimingIntervalArgs>> intervals) {
            $.intervals = intervals;
            return this;
        }

        /**
         * @param intervals The time intervals at which to mute notifications.
         * 
         * @return builder
         * 
         */
        public Builder intervals(List<MuteTimingIntervalArgs> intervals) {
            return intervals(Output.of(intervals));
        }

        /**
         * @param intervals The time intervals at which to mute notifications.
         * 
         * @return builder
         * 
         */
        public Builder intervals(MuteTimingIntervalArgs... intervals) {
            return intervals(List.of(intervals));
        }

        /**
         * @param name The name of the mute timing.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the mute timing.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public MuteTimingArgs build() {
            return $;
        }
    }

}