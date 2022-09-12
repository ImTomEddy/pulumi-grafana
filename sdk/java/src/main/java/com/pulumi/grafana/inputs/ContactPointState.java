// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.ContactPointAlertmanagerArgs;
import com.pulumi.grafana.inputs.ContactPointDingdingArgs;
import com.pulumi.grafana.inputs.ContactPointDiscordArgs;
import com.pulumi.grafana.inputs.ContactPointEmailArgs;
import com.pulumi.grafana.inputs.ContactPointGooglechatArgs;
import com.pulumi.grafana.inputs.ContactPointKafkaArgs;
import com.pulumi.grafana.inputs.ContactPointOpsgenyArgs;
import com.pulumi.grafana.inputs.ContactPointPagerdutyArgs;
import com.pulumi.grafana.inputs.ContactPointPushoverArgs;
import com.pulumi.grafana.inputs.ContactPointSensugoArgs;
import com.pulumi.grafana.inputs.ContactPointSlackArgs;
import com.pulumi.grafana.inputs.ContactPointTeamArgs;
import com.pulumi.grafana.inputs.ContactPointTelegramArgs;
import com.pulumi.grafana.inputs.ContactPointThreemaArgs;
import com.pulumi.grafana.inputs.ContactPointVictoropArgs;
import com.pulumi.grafana.inputs.ContactPointWebhookArgs;
import com.pulumi.grafana.inputs.ContactPointWecomArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContactPointState extends com.pulumi.resources.ResourceArgs {

    public static final ContactPointState Empty = new ContactPointState();

    /**
     * A contact point that sends notifications to other Alertmanager instances.
     * 
     */
    @Import(name="alertmanagers")
    private @Nullable Output<List<ContactPointAlertmanagerArgs>> alertmanagers;

    /**
     * @return A contact point that sends notifications to other Alertmanager instances.
     * 
     */
    public Optional<Output<List<ContactPointAlertmanagerArgs>>> alertmanagers() {
        return Optional.ofNullable(this.alertmanagers);
    }

    /**
     * A contact point that sends notifications to DingDing.
     * 
     */
    @Import(name="dingdings")
    private @Nullable Output<List<ContactPointDingdingArgs>> dingdings;

    /**
     * @return A contact point that sends notifications to DingDing.
     * 
     */
    public Optional<Output<List<ContactPointDingdingArgs>>> dingdings() {
        return Optional.ofNullable(this.dingdings);
    }

    /**
     * A contact point that sends notifications as Discord messages
     * 
     */
    @Import(name="discords")
    private @Nullable Output<List<ContactPointDiscordArgs>> discords;

    /**
     * @return A contact point that sends notifications as Discord messages
     * 
     */
    public Optional<Output<List<ContactPointDiscordArgs>>> discords() {
        return Optional.ofNullable(this.discords);
    }

    /**
     * A contact point that sends notifications to an email address.
     * 
     */
    @Import(name="emails")
    private @Nullable Output<List<ContactPointEmailArgs>> emails;

    /**
     * @return A contact point that sends notifications to an email address.
     * 
     */
    public Optional<Output<List<ContactPointEmailArgs>>> emails() {
        return Optional.ofNullable(this.emails);
    }

    /**
     * A contact point that sends notifications to Google Chat.
     * 
     */
    @Import(name="googlechats")
    private @Nullable Output<List<ContactPointGooglechatArgs>> googlechats;

    /**
     * @return A contact point that sends notifications to Google Chat.
     * 
     */
    public Optional<Output<List<ContactPointGooglechatArgs>>> googlechats() {
        return Optional.ofNullable(this.googlechats);
    }

    /**
     * A contact point that publishes notifications to Apache Kafka topics.
     * 
     */
    @Import(name="kafkas")
    private @Nullable Output<List<ContactPointKafkaArgs>> kafkas;

    /**
     * @return A contact point that publishes notifications to Apache Kafka topics.
     * 
     */
    public Optional<Output<List<ContactPointKafkaArgs>>> kafkas() {
        return Optional.ofNullable(this.kafkas);
    }

    /**
     * The name of the contact point.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the contact point.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * A contact point that sends notifications to OpsGenie.
     * 
     */
    @Import(name="opsgenies")
    private @Nullable Output<List<ContactPointOpsgenyArgs>> opsgenies;

    /**
     * @return A contact point that sends notifications to OpsGenie.
     * 
     */
    public Optional<Output<List<ContactPointOpsgenyArgs>>> opsgenies() {
        return Optional.ofNullable(this.opsgenies);
    }

    /**
     * A contact point that sends notifications to PagerDuty.
     * 
     */
    @Import(name="pagerduties")
    private @Nullable Output<List<ContactPointPagerdutyArgs>> pagerduties;

    /**
     * @return A contact point that sends notifications to PagerDuty.
     * 
     */
    public Optional<Output<List<ContactPointPagerdutyArgs>>> pagerduties() {
        return Optional.ofNullable(this.pagerduties);
    }

    /**
     * A contact point that sends notifications to Pushover.
     * 
     */
    @Import(name="pushovers")
    private @Nullable Output<List<ContactPointPushoverArgs>> pushovers;

    /**
     * @return A contact point that sends notifications to Pushover.
     * 
     */
    public Optional<Output<List<ContactPointPushoverArgs>>> pushovers() {
        return Optional.ofNullable(this.pushovers);
    }

    /**
     * A contact point that sends notifications to SensuGo.
     * 
     */
    @Import(name="sensugos")
    private @Nullable Output<List<ContactPointSensugoArgs>> sensugos;

    /**
     * @return A contact point that sends notifications to SensuGo.
     * 
     */
    public Optional<Output<List<ContactPointSensugoArgs>>> sensugos() {
        return Optional.ofNullable(this.sensugos);
    }

    /**
     * A contact point that sends notifications to Slack.
     * 
     */
    @Import(name="slacks")
    private @Nullable Output<List<ContactPointSlackArgs>> slacks;

    /**
     * @return A contact point that sends notifications to Slack.
     * 
     */
    public Optional<Output<List<ContactPointSlackArgs>>> slacks() {
        return Optional.ofNullable(this.slacks);
    }

    /**
     * A contact point that sends notifications to Microsoft Teams.
     * 
     */
    @Import(name="teams")
    private @Nullable Output<List<ContactPointTeamArgs>> teams;

    /**
     * @return A contact point that sends notifications to Microsoft Teams.
     * 
     */
    public Optional<Output<List<ContactPointTeamArgs>>> teams() {
        return Optional.ofNullable(this.teams);
    }

    /**
     * A contact point that sends notifications to Telegram.
     * 
     */
    @Import(name="telegrams")
    private @Nullable Output<List<ContactPointTelegramArgs>> telegrams;

    /**
     * @return A contact point that sends notifications to Telegram.
     * 
     */
    public Optional<Output<List<ContactPointTelegramArgs>>> telegrams() {
        return Optional.ofNullable(this.telegrams);
    }

    /**
     * A contact point that sends notifications to Threema.
     * 
     */
    @Import(name="threemas")
    private @Nullable Output<List<ContactPointThreemaArgs>> threemas;

    /**
     * @return A contact point that sends notifications to Threema.
     * 
     */
    public Optional<Output<List<ContactPointThreemaArgs>>> threemas() {
        return Optional.ofNullable(this.threemas);
    }

    /**
     * A contact point that sends notifications to VictorOps (now known as Splunk OnCall).
     * 
     */
    @Import(name="victorops")
    private @Nullable Output<List<ContactPointVictoropArgs>> victorops;

    /**
     * @return A contact point that sends notifications to VictorOps (now known as Splunk OnCall).
     * 
     */
    public Optional<Output<List<ContactPointVictoropArgs>>> victorops() {
        return Optional.ofNullable(this.victorops);
    }

    /**
     * A contact point that sends notifications to an arbitrary webhook, using the Prometheus webhook format defined here: https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
     * 
     */
    @Import(name="webhooks")
    private @Nullable Output<List<ContactPointWebhookArgs>> webhooks;

    /**
     * @return A contact point that sends notifications to an arbitrary webhook, using the Prometheus webhook format defined here: https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
     * 
     */
    public Optional<Output<List<ContactPointWebhookArgs>>> webhooks() {
        return Optional.ofNullable(this.webhooks);
    }

    /**
     * A contact point that sends notifications to WeCom.
     * 
     */
    @Import(name="wecoms")
    private @Nullable Output<List<ContactPointWecomArgs>> wecoms;

    /**
     * @return A contact point that sends notifications to WeCom.
     * 
     */
    public Optional<Output<List<ContactPointWecomArgs>>> wecoms() {
        return Optional.ofNullable(this.wecoms);
    }

    private ContactPointState() {}

    private ContactPointState(ContactPointState $) {
        this.alertmanagers = $.alertmanagers;
        this.dingdings = $.dingdings;
        this.discords = $.discords;
        this.emails = $.emails;
        this.googlechats = $.googlechats;
        this.kafkas = $.kafkas;
        this.name = $.name;
        this.opsgenies = $.opsgenies;
        this.pagerduties = $.pagerduties;
        this.pushovers = $.pushovers;
        this.sensugos = $.sensugos;
        this.slacks = $.slacks;
        this.teams = $.teams;
        this.telegrams = $.telegrams;
        this.threemas = $.threemas;
        this.victorops = $.victorops;
        this.webhooks = $.webhooks;
        this.wecoms = $.wecoms;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContactPointState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContactPointState $;

        public Builder() {
            $ = new ContactPointState();
        }

        public Builder(ContactPointState defaults) {
            $ = new ContactPointState(Objects.requireNonNull(defaults));
        }

        /**
         * @param alertmanagers A contact point that sends notifications to other Alertmanager instances.
         * 
         * @return builder
         * 
         */
        public Builder alertmanagers(@Nullable Output<List<ContactPointAlertmanagerArgs>> alertmanagers) {
            $.alertmanagers = alertmanagers;
            return this;
        }

        /**
         * @param alertmanagers A contact point that sends notifications to other Alertmanager instances.
         * 
         * @return builder
         * 
         */
        public Builder alertmanagers(List<ContactPointAlertmanagerArgs> alertmanagers) {
            return alertmanagers(Output.of(alertmanagers));
        }

        /**
         * @param alertmanagers A contact point that sends notifications to other Alertmanager instances.
         * 
         * @return builder
         * 
         */
        public Builder alertmanagers(ContactPointAlertmanagerArgs... alertmanagers) {
            return alertmanagers(List.of(alertmanagers));
        }

        /**
         * @param dingdings A contact point that sends notifications to DingDing.
         * 
         * @return builder
         * 
         */
        public Builder dingdings(@Nullable Output<List<ContactPointDingdingArgs>> dingdings) {
            $.dingdings = dingdings;
            return this;
        }

        /**
         * @param dingdings A contact point that sends notifications to DingDing.
         * 
         * @return builder
         * 
         */
        public Builder dingdings(List<ContactPointDingdingArgs> dingdings) {
            return dingdings(Output.of(dingdings));
        }

        /**
         * @param dingdings A contact point that sends notifications to DingDing.
         * 
         * @return builder
         * 
         */
        public Builder dingdings(ContactPointDingdingArgs... dingdings) {
            return dingdings(List.of(dingdings));
        }

        /**
         * @param discords A contact point that sends notifications as Discord messages
         * 
         * @return builder
         * 
         */
        public Builder discords(@Nullable Output<List<ContactPointDiscordArgs>> discords) {
            $.discords = discords;
            return this;
        }

        /**
         * @param discords A contact point that sends notifications as Discord messages
         * 
         * @return builder
         * 
         */
        public Builder discords(List<ContactPointDiscordArgs> discords) {
            return discords(Output.of(discords));
        }

        /**
         * @param discords A contact point that sends notifications as Discord messages
         * 
         * @return builder
         * 
         */
        public Builder discords(ContactPointDiscordArgs... discords) {
            return discords(List.of(discords));
        }

        /**
         * @param emails A contact point that sends notifications to an email address.
         * 
         * @return builder
         * 
         */
        public Builder emails(@Nullable Output<List<ContactPointEmailArgs>> emails) {
            $.emails = emails;
            return this;
        }

        /**
         * @param emails A contact point that sends notifications to an email address.
         * 
         * @return builder
         * 
         */
        public Builder emails(List<ContactPointEmailArgs> emails) {
            return emails(Output.of(emails));
        }

        /**
         * @param emails A contact point that sends notifications to an email address.
         * 
         * @return builder
         * 
         */
        public Builder emails(ContactPointEmailArgs... emails) {
            return emails(List.of(emails));
        }

        /**
         * @param googlechats A contact point that sends notifications to Google Chat.
         * 
         * @return builder
         * 
         */
        public Builder googlechats(@Nullable Output<List<ContactPointGooglechatArgs>> googlechats) {
            $.googlechats = googlechats;
            return this;
        }

        /**
         * @param googlechats A contact point that sends notifications to Google Chat.
         * 
         * @return builder
         * 
         */
        public Builder googlechats(List<ContactPointGooglechatArgs> googlechats) {
            return googlechats(Output.of(googlechats));
        }

        /**
         * @param googlechats A contact point that sends notifications to Google Chat.
         * 
         * @return builder
         * 
         */
        public Builder googlechats(ContactPointGooglechatArgs... googlechats) {
            return googlechats(List.of(googlechats));
        }

        /**
         * @param kafkas A contact point that publishes notifications to Apache Kafka topics.
         * 
         * @return builder
         * 
         */
        public Builder kafkas(@Nullable Output<List<ContactPointKafkaArgs>> kafkas) {
            $.kafkas = kafkas;
            return this;
        }

        /**
         * @param kafkas A contact point that publishes notifications to Apache Kafka topics.
         * 
         * @return builder
         * 
         */
        public Builder kafkas(List<ContactPointKafkaArgs> kafkas) {
            return kafkas(Output.of(kafkas));
        }

        /**
         * @param kafkas A contact point that publishes notifications to Apache Kafka topics.
         * 
         * @return builder
         * 
         */
        public Builder kafkas(ContactPointKafkaArgs... kafkas) {
            return kafkas(List.of(kafkas));
        }

        /**
         * @param name The name of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param opsgenies A contact point that sends notifications to OpsGenie.
         * 
         * @return builder
         * 
         */
        public Builder opsgenies(@Nullable Output<List<ContactPointOpsgenyArgs>> opsgenies) {
            $.opsgenies = opsgenies;
            return this;
        }

        /**
         * @param opsgenies A contact point that sends notifications to OpsGenie.
         * 
         * @return builder
         * 
         */
        public Builder opsgenies(List<ContactPointOpsgenyArgs> opsgenies) {
            return opsgenies(Output.of(opsgenies));
        }

        /**
         * @param opsgenies A contact point that sends notifications to OpsGenie.
         * 
         * @return builder
         * 
         */
        public Builder opsgenies(ContactPointOpsgenyArgs... opsgenies) {
            return opsgenies(List.of(opsgenies));
        }

        /**
         * @param pagerduties A contact point that sends notifications to PagerDuty.
         * 
         * @return builder
         * 
         */
        public Builder pagerduties(@Nullable Output<List<ContactPointPagerdutyArgs>> pagerduties) {
            $.pagerduties = pagerduties;
            return this;
        }

        /**
         * @param pagerduties A contact point that sends notifications to PagerDuty.
         * 
         * @return builder
         * 
         */
        public Builder pagerduties(List<ContactPointPagerdutyArgs> pagerduties) {
            return pagerduties(Output.of(pagerduties));
        }

        /**
         * @param pagerduties A contact point that sends notifications to PagerDuty.
         * 
         * @return builder
         * 
         */
        public Builder pagerduties(ContactPointPagerdutyArgs... pagerduties) {
            return pagerduties(List.of(pagerduties));
        }

        /**
         * @param pushovers A contact point that sends notifications to Pushover.
         * 
         * @return builder
         * 
         */
        public Builder pushovers(@Nullable Output<List<ContactPointPushoverArgs>> pushovers) {
            $.pushovers = pushovers;
            return this;
        }

        /**
         * @param pushovers A contact point that sends notifications to Pushover.
         * 
         * @return builder
         * 
         */
        public Builder pushovers(List<ContactPointPushoverArgs> pushovers) {
            return pushovers(Output.of(pushovers));
        }

        /**
         * @param pushovers A contact point that sends notifications to Pushover.
         * 
         * @return builder
         * 
         */
        public Builder pushovers(ContactPointPushoverArgs... pushovers) {
            return pushovers(List.of(pushovers));
        }

        /**
         * @param sensugos A contact point that sends notifications to SensuGo.
         * 
         * @return builder
         * 
         */
        public Builder sensugos(@Nullable Output<List<ContactPointSensugoArgs>> sensugos) {
            $.sensugos = sensugos;
            return this;
        }

        /**
         * @param sensugos A contact point that sends notifications to SensuGo.
         * 
         * @return builder
         * 
         */
        public Builder sensugos(List<ContactPointSensugoArgs> sensugos) {
            return sensugos(Output.of(sensugos));
        }

        /**
         * @param sensugos A contact point that sends notifications to SensuGo.
         * 
         * @return builder
         * 
         */
        public Builder sensugos(ContactPointSensugoArgs... sensugos) {
            return sensugos(List.of(sensugos));
        }

        /**
         * @param slacks A contact point that sends notifications to Slack.
         * 
         * @return builder
         * 
         */
        public Builder slacks(@Nullable Output<List<ContactPointSlackArgs>> slacks) {
            $.slacks = slacks;
            return this;
        }

        /**
         * @param slacks A contact point that sends notifications to Slack.
         * 
         * @return builder
         * 
         */
        public Builder slacks(List<ContactPointSlackArgs> slacks) {
            return slacks(Output.of(slacks));
        }

        /**
         * @param slacks A contact point that sends notifications to Slack.
         * 
         * @return builder
         * 
         */
        public Builder slacks(ContactPointSlackArgs... slacks) {
            return slacks(List.of(slacks));
        }

        /**
         * @param teams A contact point that sends notifications to Microsoft Teams.
         * 
         * @return builder
         * 
         */
        public Builder teams(@Nullable Output<List<ContactPointTeamArgs>> teams) {
            $.teams = teams;
            return this;
        }

        /**
         * @param teams A contact point that sends notifications to Microsoft Teams.
         * 
         * @return builder
         * 
         */
        public Builder teams(List<ContactPointTeamArgs> teams) {
            return teams(Output.of(teams));
        }

        /**
         * @param teams A contact point that sends notifications to Microsoft Teams.
         * 
         * @return builder
         * 
         */
        public Builder teams(ContactPointTeamArgs... teams) {
            return teams(List.of(teams));
        }

        /**
         * @param telegrams A contact point that sends notifications to Telegram.
         * 
         * @return builder
         * 
         */
        public Builder telegrams(@Nullable Output<List<ContactPointTelegramArgs>> telegrams) {
            $.telegrams = telegrams;
            return this;
        }

        /**
         * @param telegrams A contact point that sends notifications to Telegram.
         * 
         * @return builder
         * 
         */
        public Builder telegrams(List<ContactPointTelegramArgs> telegrams) {
            return telegrams(Output.of(telegrams));
        }

        /**
         * @param telegrams A contact point that sends notifications to Telegram.
         * 
         * @return builder
         * 
         */
        public Builder telegrams(ContactPointTelegramArgs... telegrams) {
            return telegrams(List.of(telegrams));
        }

        /**
         * @param threemas A contact point that sends notifications to Threema.
         * 
         * @return builder
         * 
         */
        public Builder threemas(@Nullable Output<List<ContactPointThreemaArgs>> threemas) {
            $.threemas = threemas;
            return this;
        }

        /**
         * @param threemas A contact point that sends notifications to Threema.
         * 
         * @return builder
         * 
         */
        public Builder threemas(List<ContactPointThreemaArgs> threemas) {
            return threemas(Output.of(threemas));
        }

        /**
         * @param threemas A contact point that sends notifications to Threema.
         * 
         * @return builder
         * 
         */
        public Builder threemas(ContactPointThreemaArgs... threemas) {
            return threemas(List.of(threemas));
        }

        /**
         * @param victorops A contact point that sends notifications to VictorOps (now known as Splunk OnCall).
         * 
         * @return builder
         * 
         */
        public Builder victorops(@Nullable Output<List<ContactPointVictoropArgs>> victorops) {
            $.victorops = victorops;
            return this;
        }

        /**
         * @param victorops A contact point that sends notifications to VictorOps (now known as Splunk OnCall).
         * 
         * @return builder
         * 
         */
        public Builder victorops(List<ContactPointVictoropArgs> victorops) {
            return victorops(Output.of(victorops));
        }

        /**
         * @param victorops A contact point that sends notifications to VictorOps (now known as Splunk OnCall).
         * 
         * @return builder
         * 
         */
        public Builder victorops(ContactPointVictoropArgs... victorops) {
            return victorops(List.of(victorops));
        }

        /**
         * @param webhooks A contact point that sends notifications to an arbitrary webhook, using the Prometheus webhook format defined here: https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
         * 
         * @return builder
         * 
         */
        public Builder webhooks(@Nullable Output<List<ContactPointWebhookArgs>> webhooks) {
            $.webhooks = webhooks;
            return this;
        }

        /**
         * @param webhooks A contact point that sends notifications to an arbitrary webhook, using the Prometheus webhook format defined here: https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
         * 
         * @return builder
         * 
         */
        public Builder webhooks(List<ContactPointWebhookArgs> webhooks) {
            return webhooks(Output.of(webhooks));
        }

        /**
         * @param webhooks A contact point that sends notifications to an arbitrary webhook, using the Prometheus webhook format defined here: https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
         * 
         * @return builder
         * 
         */
        public Builder webhooks(ContactPointWebhookArgs... webhooks) {
            return webhooks(List.of(webhooks));
        }

        /**
         * @param wecoms A contact point that sends notifications to WeCom.
         * 
         * @return builder
         * 
         */
        public Builder wecoms(@Nullable Output<List<ContactPointWecomArgs>> wecoms) {
            $.wecoms = wecoms;
            return this;
        }

        /**
         * @param wecoms A contact point that sends notifications to WeCom.
         * 
         * @return builder
         * 
         */
        public Builder wecoms(List<ContactPointWecomArgs> wecoms) {
            return wecoms(Output.of(wecoms));
        }

        /**
         * @param wecoms A contact point that sends notifications to WeCom.
         * 
         * @return builder
         * 
         */
        public Builder wecoms(ContactPointWecomArgs... wecoms) {
            return wecoms(List.of(wecoms));
        }

        public ContactPointState build() {
            return $;
        }
    }

}