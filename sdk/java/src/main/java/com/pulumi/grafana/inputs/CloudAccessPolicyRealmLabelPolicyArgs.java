// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;


public final class CloudAccessPolicyRealmLabelPolicyArgs extends com.pulumi.resources.ResourceArgs {

    public static final CloudAccessPolicyRealmLabelPolicyArgs Empty = new CloudAccessPolicyRealmLabelPolicyArgs();

    @Import(name="selector", required=true)
    private Output<String> selector;

    public Output<String> selector() {
        return this.selector;
    }

    private CloudAccessPolicyRealmLabelPolicyArgs() {}

    private CloudAccessPolicyRealmLabelPolicyArgs(CloudAccessPolicyRealmLabelPolicyArgs $) {
        this.selector = $.selector;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(CloudAccessPolicyRealmLabelPolicyArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private CloudAccessPolicyRealmLabelPolicyArgs $;

        public Builder() {
            $ = new CloudAccessPolicyRealmLabelPolicyArgs();
        }

        public Builder(CloudAccessPolicyRealmLabelPolicyArgs defaults) {
            $ = new CloudAccessPolicyRealmLabelPolicyArgs(Objects.requireNonNull(defaults));
        }

        public Builder selector(Output<String> selector) {
            $.selector = selector;
            return this;
        }

        public Builder selector(String selector) {
            return selector(Output.of(selector));
        }

        public CloudAccessPolicyRealmLabelPolicyArgs build() {
            $.selector = Objects.requireNonNull($.selector, "expected parameter 'selector' to be non-null");
            return $;
        }
    }

}