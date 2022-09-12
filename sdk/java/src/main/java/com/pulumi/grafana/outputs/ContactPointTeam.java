// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ContactPointTeam {
    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    private @Nullable Boolean disableResolveMessage;
    /**
     * @return The templated message content to send.
     * 
     */
    private @Nullable String message;
    /**
     * @return The templated subtitle for each message section.
     * 
     */
    private @Nullable String sectionTitle;
    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    private @Nullable Map<String,String> settings;
    /**
     * @return The templated title of the message.
     * 
     */
    private @Nullable String title;
    /**
     * @return The UID of the contact point.
     * 
     */
    private @Nullable String uid;
    /**
     * @return A Teams webhook URL.
     * 
     */
    private String url;

    private ContactPointTeam() {}
    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    public Optional<Boolean> disableResolveMessage() {
        return Optional.ofNullable(this.disableResolveMessage);
    }
    /**
     * @return The templated message content to send.
     * 
     */
    public Optional<String> message() {
        return Optional.ofNullable(this.message);
    }
    /**
     * @return The templated subtitle for each message section.
     * 
     */
    public Optional<String> sectionTitle() {
        return Optional.ofNullable(this.sectionTitle);
    }
    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    public Map<String,String> settings() {
        return this.settings == null ? Map.of() : this.settings;
    }
    /**
     * @return The templated title of the message.
     * 
     */
    public Optional<String> title() {
        return Optional.ofNullable(this.title);
    }
    /**
     * @return The UID of the contact point.
     * 
     */
    public Optional<String> uid() {
        return Optional.ofNullable(this.uid);
    }
    /**
     * @return A Teams webhook URL.
     * 
     */
    public String url() {
        return this.url;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ContactPointTeam defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean disableResolveMessage;
        private @Nullable String message;
        private @Nullable String sectionTitle;
        private @Nullable Map<String,String> settings;
        private @Nullable String title;
        private @Nullable String uid;
        private String url;
        public Builder() {}
        public Builder(ContactPointTeam defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.disableResolveMessage = defaults.disableResolveMessage;
    	      this.message = defaults.message;
    	      this.sectionTitle = defaults.sectionTitle;
    	      this.settings = defaults.settings;
    	      this.title = defaults.title;
    	      this.uid = defaults.uid;
    	      this.url = defaults.url;
        }

        @CustomType.Setter
        public Builder disableResolveMessage(@Nullable Boolean disableResolveMessage) {
            this.disableResolveMessage = disableResolveMessage;
            return this;
        }
        @CustomType.Setter
        public Builder message(@Nullable String message) {
            this.message = message;
            return this;
        }
        @CustomType.Setter
        public Builder sectionTitle(@Nullable String sectionTitle) {
            this.sectionTitle = sectionTitle;
            return this;
        }
        @CustomType.Setter
        public Builder settings(@Nullable Map<String,String> settings) {
            this.settings = settings;
            return this;
        }
        @CustomType.Setter
        public Builder title(@Nullable String title) {
            this.title = title;
            return this;
        }
        @CustomType.Setter
        public Builder uid(@Nullable String uid) {
            this.uid = uid;
            return this;
        }
        @CustomType.Setter
        public Builder url(String url) {
            this.url = Objects.requireNonNull(url);
            return this;
        }
        public ContactPointTeam build() {
            final var o = new ContactPointTeam();
            o.disableResolveMessage = disableResolveMessage;
            o.message = message;
            o.sectionTitle = sectionTitle;
            o.settings = settings;
            o.title = title;
            o.uid = uid;
            o.url = url;
            return o;
        }
    }
}