// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ContactPointPushover {
    /**
     * @return The Pushover API token.
     * 
     */
    private String apiToken;
    /**
     * @return Comma-separated list of devices to which the event is associated.
     * 
     */
    private @Nullable String device;
    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    private @Nullable Boolean disableResolveMessage;
    /**
     * @return How many seconds for which the notification will continue to be retried by Pushover.
     * 
     */
    private @Nullable Integer expire;
    /**
     * @return The templated notification message content.
     * 
     */
    private @Nullable String message;
    /**
     * @return The priority level of the resolved event.
     * 
     */
    private @Nullable Integer okPriority;
    /**
     * @return The sound associated with the resolved notification.
     * 
     */
    private @Nullable String okSound;
    /**
     * @return The priority level of the event.
     * 
     */
    private @Nullable Integer priority;
    /**
     * @return How often, in seconds, the Pushover servers will send the same notification to the user.
     * 
     */
    private @Nullable Integer retry;
    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    private @Nullable Map<String,String> settings;
    /**
     * @return The sound associated with the notification.
     * 
     */
    private @Nullable String sound;
    /**
     * @return The UID of the contact point.
     * 
     */
    private @Nullable String uid;
    /**
     * @return The Pushover user key.
     * 
     */
    private String userKey;

    private ContactPointPushover() {}
    /**
     * @return The Pushover API token.
     * 
     */
    public String apiToken() {
        return this.apiToken;
    }
    /**
     * @return Comma-separated list of devices to which the event is associated.
     * 
     */
    public Optional<String> device() {
        return Optional.ofNullable(this.device);
    }
    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    public Optional<Boolean> disableResolveMessage() {
        return Optional.ofNullable(this.disableResolveMessage);
    }
    /**
     * @return How many seconds for which the notification will continue to be retried by Pushover.
     * 
     */
    public Optional<Integer> expire() {
        return Optional.ofNullable(this.expire);
    }
    /**
     * @return The templated notification message content.
     * 
     */
    public Optional<String> message() {
        return Optional.ofNullable(this.message);
    }
    /**
     * @return The priority level of the resolved event.
     * 
     */
    public Optional<Integer> okPriority() {
        return Optional.ofNullable(this.okPriority);
    }
    /**
     * @return The sound associated with the resolved notification.
     * 
     */
    public Optional<String> okSound() {
        return Optional.ofNullable(this.okSound);
    }
    /**
     * @return The priority level of the event.
     * 
     */
    public Optional<Integer> priority() {
        return Optional.ofNullable(this.priority);
    }
    /**
     * @return How often, in seconds, the Pushover servers will send the same notification to the user.
     * 
     */
    public Optional<Integer> retry() {
        return Optional.ofNullable(this.retry);
    }
    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    public Map<String,String> settings() {
        return this.settings == null ? Map.of() : this.settings;
    }
    /**
     * @return The sound associated with the notification.
     * 
     */
    public Optional<String> sound() {
        return Optional.ofNullable(this.sound);
    }
    /**
     * @return The UID of the contact point.
     * 
     */
    public Optional<String> uid() {
        return Optional.ofNullable(this.uid);
    }
    /**
     * @return The Pushover user key.
     * 
     */
    public String userKey() {
        return this.userKey;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ContactPointPushover defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String apiToken;
        private @Nullable String device;
        private @Nullable Boolean disableResolveMessage;
        private @Nullable Integer expire;
        private @Nullable String message;
        private @Nullable Integer okPriority;
        private @Nullable String okSound;
        private @Nullable Integer priority;
        private @Nullable Integer retry;
        private @Nullable Map<String,String> settings;
        private @Nullable String sound;
        private @Nullable String uid;
        private String userKey;
        public Builder() {}
        public Builder(ContactPointPushover defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.apiToken = defaults.apiToken;
    	      this.device = defaults.device;
    	      this.disableResolveMessage = defaults.disableResolveMessage;
    	      this.expire = defaults.expire;
    	      this.message = defaults.message;
    	      this.okPriority = defaults.okPriority;
    	      this.okSound = defaults.okSound;
    	      this.priority = defaults.priority;
    	      this.retry = defaults.retry;
    	      this.settings = defaults.settings;
    	      this.sound = defaults.sound;
    	      this.uid = defaults.uid;
    	      this.userKey = defaults.userKey;
        }

        @CustomType.Setter
        public Builder apiToken(String apiToken) {
            this.apiToken = Objects.requireNonNull(apiToken);
            return this;
        }
        @CustomType.Setter
        public Builder device(@Nullable String device) {
            this.device = device;
            return this;
        }
        @CustomType.Setter
        public Builder disableResolveMessage(@Nullable Boolean disableResolveMessage) {
            this.disableResolveMessage = disableResolveMessage;
            return this;
        }
        @CustomType.Setter
        public Builder expire(@Nullable Integer expire) {
            this.expire = expire;
            return this;
        }
        @CustomType.Setter
        public Builder message(@Nullable String message) {
            this.message = message;
            return this;
        }
        @CustomType.Setter
        public Builder okPriority(@Nullable Integer okPriority) {
            this.okPriority = okPriority;
            return this;
        }
        @CustomType.Setter
        public Builder okSound(@Nullable String okSound) {
            this.okSound = okSound;
            return this;
        }
        @CustomType.Setter
        public Builder priority(@Nullable Integer priority) {
            this.priority = priority;
            return this;
        }
        @CustomType.Setter
        public Builder retry(@Nullable Integer retry) {
            this.retry = retry;
            return this;
        }
        @CustomType.Setter
        public Builder settings(@Nullable Map<String,String> settings) {
            this.settings = settings;
            return this;
        }
        @CustomType.Setter
        public Builder sound(@Nullable String sound) {
            this.sound = sound;
            return this;
        }
        @CustomType.Setter
        public Builder uid(@Nullable String uid) {
            this.uid = uid;
            return this;
        }
        @CustomType.Setter
        public Builder userKey(String userKey) {
            this.userKey = Objects.requireNonNull(userKey);
            return this;
        }
        public ContactPointPushover build() {
            final var o = new ContactPointPushover();
            o.apiToken = apiToken;
            o.device = device;
            o.disableResolveMessage = disableResolveMessage;
            o.expire = expire;
            o.message = message;
            o.okPriority = okPriority;
            o.okSound = okSound;
            o.priority = priority;
            o.retry = retry;
            o.settings = settings;
            o.sound = sound;
            o.uid = uid;
            o.userKey = userKey;
            return o;
        }
    }
}