// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Object;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AlertNotificationState extends com.pulumi.resources.ResourceArgs {

    public static final AlertNotificationState Empty = new AlertNotificationState();

    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    @Import(name="disableResolveMessage")
    private @Nullable Output<Boolean> disableResolveMessage;

    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> disableResolveMessage() {
        return Optional.ofNullable(this.disableResolveMessage);
    }

    /**
     * Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     * 
     */
    @Import(name="frequency")
    private @Nullable Output<String> frequency;

    /**
     * @return Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     * 
     */
    public Optional<Output<String>> frequency() {
        return Optional.ofNullable(this.frequency);
    }

    /**
     * Is this the default channel for all your alerts. Defaults to `false`.
     * 
     */
    @Import(name="isDefault")
    private @Nullable Output<Boolean> isDefault;

    /**
     * @return Is this the default channel for all your alerts. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> isDefault() {
        return Optional.ofNullable(this.isDefault);
    }

    /**
     * The name of the alert notification channel.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the alert notification channel.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     * 
     */
    @Import(name="secureSettings")
    private @Nullable Output<Map<String,Object>> secureSettings;

    /**
     * @return Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     * 
     */
    public Optional<Output<Map<String,Object>>> secureSettings() {
        return Optional.ofNullable(this.secureSettings);
    }

    /**
     * Whether to send reminders for triggered alerts. Defaults to `false`.
     * 
     */
    @Import(name="sendReminder")
    private @Nullable Output<Boolean> sendReminder;

    /**
     * @return Whether to send reminders for triggered alerts. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> sendReminder() {
        return Optional.ofNullable(this.sendReminder);
    }

    /**
     * Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
     * 
     */
    @Import(name="settings")
    private @Nullable Output<Map<String,Object>> settings;

    /**
     * @return Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
     * 
     */
    public Optional<Output<Map<String,Object>>> settings() {
        return Optional.ofNullable(this.settings);
    }

    /**
     * The type of the alert notification channel.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return The type of the alert notification channel.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    /**
     * Unique identifier. If unset, this will be automatically generated.
     * 
     */
    @Import(name="uid")
    private @Nullable Output<String> uid;

    /**
     * @return Unique identifier. If unset, this will be automatically generated.
     * 
     */
    public Optional<Output<String>> uid() {
        return Optional.ofNullable(this.uid);
    }

    private AlertNotificationState() {}

    private AlertNotificationState(AlertNotificationState $) {
        this.disableResolveMessage = $.disableResolveMessage;
        this.frequency = $.frequency;
        this.isDefault = $.isDefault;
        this.name = $.name;
        this.secureSettings = $.secureSettings;
        this.sendReminder = $.sendReminder;
        this.settings = $.settings;
        this.type = $.type;
        this.uid = $.uid;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AlertNotificationState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AlertNotificationState $;

        public Builder() {
            $ = new AlertNotificationState();
        }

        public Builder(AlertNotificationState defaults) {
            $ = new AlertNotificationState(Objects.requireNonNull(defaults));
        }

        /**
         * @param disableResolveMessage Whether to disable sending resolve messages. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder disableResolveMessage(@Nullable Output<Boolean> disableResolveMessage) {
            $.disableResolveMessage = disableResolveMessage;
            return this;
        }

        /**
         * @param disableResolveMessage Whether to disable sending resolve messages. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder disableResolveMessage(Boolean disableResolveMessage) {
            return disableResolveMessage(Output.of(disableResolveMessage));
        }

        /**
         * @param frequency Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
         * 
         * @return builder
         * 
         */
        public Builder frequency(@Nullable Output<String> frequency) {
            $.frequency = frequency;
            return this;
        }

        /**
         * @param frequency Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
         * 
         * @return builder
         * 
         */
        public Builder frequency(String frequency) {
            return frequency(Output.of(frequency));
        }

        /**
         * @param isDefault Is this the default channel for all your alerts. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder isDefault(@Nullable Output<Boolean> isDefault) {
            $.isDefault = isDefault;
            return this;
        }

        /**
         * @param isDefault Is this the default channel for all your alerts. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder isDefault(Boolean isDefault) {
            return isDefault(Output.of(isDefault));
        }

        /**
         * @param name The name of the alert notification channel.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the alert notification channel.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param secureSettings Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
         * 
         * @return builder
         * 
         */
        public Builder secureSettings(@Nullable Output<Map<String,Object>> secureSettings) {
            $.secureSettings = secureSettings;
            return this;
        }

        /**
         * @param secureSettings Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
         * 
         * @return builder
         * 
         */
        public Builder secureSettings(Map<String,Object> secureSettings) {
            return secureSettings(Output.of(secureSettings));
        }

        /**
         * @param sendReminder Whether to send reminders for triggered alerts. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder sendReminder(@Nullable Output<Boolean> sendReminder) {
            $.sendReminder = sendReminder;
            return this;
        }

        /**
         * @param sendReminder Whether to send reminders for triggered alerts. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder sendReminder(Boolean sendReminder) {
            return sendReminder(Output.of(sendReminder));
        }

        /**
         * @param settings Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
         * 
         * @return builder
         * 
         */
        public Builder settings(@Nullable Output<Map<String,Object>> settings) {
            $.settings = settings;
            return this;
        }

        /**
         * @param settings Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
         * 
         * @return builder
         * 
         */
        public Builder settings(Map<String,Object> settings) {
            return settings(Output.of(settings));
        }

        /**
         * @param type The type of the alert notification channel.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The type of the alert notification channel.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param uid Unique identifier. If unset, this will be automatically generated.
         * 
         * @return builder
         * 
         */
        public Builder uid(@Nullable Output<String> uid) {
            $.uid = uid;
            return this;
        }

        /**
         * @param uid Unique identifier. If unset, this will be automatically generated.
         * 
         * @return builder
         * 
         */
        public Builder uid(String uid) {
            return uid(Output.of(uid));
        }

        public AlertNotificationState build() {
            return $;
        }
    }

}