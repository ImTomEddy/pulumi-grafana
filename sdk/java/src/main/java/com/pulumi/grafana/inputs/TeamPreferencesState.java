// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class TeamPreferencesState extends com.pulumi.resources.ResourceArgs {

    public static final TeamPreferencesState Empty = new TeamPreferencesState();

    /**
     * The numeric ID of the dashboard to display when a team member logs in.
     * 
     */
    @Import(name="homeDashboardId")
    private @Nullable Output<Integer> homeDashboardId;

    /**
     * @return The numeric ID of the dashboard to display when a team member logs in.
     * 
     */
    public Optional<Output<Integer>> homeDashboardId() {
        return Optional.ofNullable(this.homeDashboardId);
    }

    /**
     * The numeric team ID.
     * 
     */
    @Import(name="teamId")
    private @Nullable Output<Integer> teamId;

    /**
     * @return The numeric team ID.
     * 
     */
    public Optional<Output<Integer>> teamId() {
        return Optional.ofNullable(this.teamId);
    }

    /**
     * The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
     * 
     */
    @Import(name="theme")
    private @Nullable Output<String> theme;

    /**
     * @return The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
     * 
     */
    public Optional<Output<String>> theme() {
        return Optional.ofNullable(this.theme);
    }

    /**
     * The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
     * 
     */
    @Import(name="timezone")
    private @Nullable Output<String> timezone;

    /**
     * @return The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
     * 
     */
    public Optional<Output<String>> timezone() {
        return Optional.ofNullable(this.timezone);
    }

    private TeamPreferencesState() {}

    private TeamPreferencesState(TeamPreferencesState $) {
        this.homeDashboardId = $.homeDashboardId;
        this.teamId = $.teamId;
        this.theme = $.theme;
        this.timezone = $.timezone;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(TeamPreferencesState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private TeamPreferencesState $;

        public Builder() {
            $ = new TeamPreferencesState();
        }

        public Builder(TeamPreferencesState defaults) {
            $ = new TeamPreferencesState(Objects.requireNonNull(defaults));
        }

        /**
         * @param homeDashboardId The numeric ID of the dashboard to display when a team member logs in.
         * 
         * @return builder
         * 
         */
        public Builder homeDashboardId(@Nullable Output<Integer> homeDashboardId) {
            $.homeDashboardId = homeDashboardId;
            return this;
        }

        /**
         * @param homeDashboardId The numeric ID of the dashboard to display when a team member logs in.
         * 
         * @return builder
         * 
         */
        public Builder homeDashboardId(Integer homeDashboardId) {
            return homeDashboardId(Output.of(homeDashboardId));
        }

        /**
         * @param teamId The numeric team ID.
         * 
         * @return builder
         * 
         */
        public Builder teamId(@Nullable Output<Integer> teamId) {
            $.teamId = teamId;
            return this;
        }

        /**
         * @param teamId The numeric team ID.
         * 
         * @return builder
         * 
         */
        public Builder teamId(Integer teamId) {
            return teamId(Output.of(teamId));
        }

        /**
         * @param theme The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
         * 
         * @return builder
         * 
         */
        public Builder theme(@Nullable Output<String> theme) {
            $.theme = theme;
            return this;
        }

        /**
         * @param theme The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
         * 
         * @return builder
         * 
         */
        public Builder theme(String theme) {
            return theme(Output.of(theme));
        }

        /**
         * @param timezone The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
         * 
         * @return builder
         * 
         */
        public Builder timezone(@Nullable Output<String> timezone) {
            $.timezone = timezone;
            return this;
        }

        /**
         * @param timezone The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
         * 
         * @return builder
         * 
         */
        public Builder timezone(String timezone) {
            return timezone(Output.of(timezone));
        }

        public TeamPreferencesState build() {
            return $;
        }
    }

}