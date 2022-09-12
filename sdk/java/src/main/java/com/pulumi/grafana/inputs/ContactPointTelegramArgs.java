// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContactPointTelegramArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContactPointTelegramArgs Empty = new ContactPointTelegramArgs();

    /**
     * The chat ID to send messages to.
     * 
     */
    @Import(name="chatId", required=true)
    private Output<String> chatId;

    /**
     * @return The chat ID to send messages to.
     * 
     */
    public Output<String> chatId() {
        return this.chatId;
    }

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
     * The templated content of the message.
     * 
     */
    @Import(name="message")
    private @Nullable Output<String> message;

    /**
     * @return The templated content of the message.
     * 
     */
    public Optional<Output<String>> message() {
        return Optional.ofNullable(this.message);
    }

    /**
     * Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    @Import(name="settings")
    private @Nullable Output<Map<String,String>> settings;

    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    public Optional<Output<Map<String,String>>> settings() {
        return Optional.ofNullable(this.settings);
    }

    /**
     * The Telegram bot token.
     * 
     */
    @Import(name="token", required=true)
    private Output<String> token;

    /**
     * @return The Telegram bot token.
     * 
     */
    public Output<String> token() {
        return this.token;
    }

    /**
     * The UID of the contact point.
     * 
     */
    @Import(name="uid")
    private @Nullable Output<String> uid;

    /**
     * @return The UID of the contact point.
     * 
     */
    public Optional<Output<String>> uid() {
        return Optional.ofNullable(this.uid);
    }

    private ContactPointTelegramArgs() {}

    private ContactPointTelegramArgs(ContactPointTelegramArgs $) {
        this.chatId = $.chatId;
        this.disableResolveMessage = $.disableResolveMessage;
        this.message = $.message;
        this.settings = $.settings;
        this.token = $.token;
        this.uid = $.uid;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContactPointTelegramArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContactPointTelegramArgs $;

        public Builder() {
            $ = new ContactPointTelegramArgs();
        }

        public Builder(ContactPointTelegramArgs defaults) {
            $ = new ContactPointTelegramArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param chatId The chat ID to send messages to.
         * 
         * @return builder
         * 
         */
        public Builder chatId(Output<String> chatId) {
            $.chatId = chatId;
            return this;
        }

        /**
         * @param chatId The chat ID to send messages to.
         * 
         * @return builder
         * 
         */
        public Builder chatId(String chatId) {
            return chatId(Output.of(chatId));
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
         * @param message The templated content of the message.
         * 
         * @return builder
         * 
         */
        public Builder message(@Nullable Output<String> message) {
            $.message = message;
            return this;
        }

        /**
         * @param message The templated content of the message.
         * 
         * @return builder
         * 
         */
        public Builder message(String message) {
            return message(Output.of(message));
        }

        /**
         * @param settings Additional custom properties to attach to the notifier. Defaults to `map[]`.
         * 
         * @return builder
         * 
         */
        public Builder settings(@Nullable Output<Map<String,String>> settings) {
            $.settings = settings;
            return this;
        }

        /**
         * @param settings Additional custom properties to attach to the notifier. Defaults to `map[]`.
         * 
         * @return builder
         * 
         */
        public Builder settings(Map<String,String> settings) {
            return settings(Output.of(settings));
        }

        /**
         * @param token The Telegram bot token.
         * 
         * @return builder
         * 
         */
        public Builder token(Output<String> token) {
            $.token = token;
            return this;
        }

        /**
         * @param token The Telegram bot token.
         * 
         * @return builder
         * 
         */
        public Builder token(String token) {
            return token(Output.of(token));
        }

        /**
         * @param uid The UID of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder uid(@Nullable Output<String> uid) {
            $.uid = uid;
            return this;
        }

        /**
         * @param uid The UID of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder uid(String uid) {
            return uid(Output.of(uid));
        }

        public ContactPointTelegramArgs build() {
            $.chatId = Objects.requireNonNull($.chatId, "expected parameter 'chatId' to be non-null");
            $.token = Objects.requireNonNull($.token, "expected parameter 'token' to be non-null");
            return $;
        }
    }

}