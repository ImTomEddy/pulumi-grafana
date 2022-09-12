// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MessageTemplateArgs extends com.pulumi.resources.ResourceArgs {

    public static final MessageTemplateArgs Empty = new MessageTemplateArgs();

    /**
     * The name of the message template.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the message template.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The content of the message template.
     * 
     */
    @Import(name="template", required=true)
    private Output<String> template;

    /**
     * @return The content of the message template.
     * 
     */
    public Output<String> template() {
        return this.template;
    }

    private MessageTemplateArgs() {}

    private MessageTemplateArgs(MessageTemplateArgs $) {
        this.name = $.name;
        this.template = $.template;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MessageTemplateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MessageTemplateArgs $;

        public Builder() {
            $ = new MessageTemplateArgs();
        }

        public Builder(MessageTemplateArgs defaults) {
            $ = new MessageTemplateArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name The name of the message template.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the message template.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param template The content of the message template.
         * 
         * @return builder
         * 
         */
        public Builder template(Output<String> template) {
            $.template = template;
            return this;
        }

        /**
         * @param template The content of the message template.
         * 
         * @return builder
         * 
         */
        public Builder template(String template) {
            return template(Output.of(template));
        }

        public MessageTemplateArgs build() {
            $.template = Objects.requireNonNull($.template, "expected parameter 'template' to be non-null");
            return $;
        }
    }

}