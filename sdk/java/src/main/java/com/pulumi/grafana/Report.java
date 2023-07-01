// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.ReportArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.ReportState;
import com.pulumi.grafana.outputs.ReportSchedule;
import com.pulumi.grafana.outputs.ReportTimeRange;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * **Note:** This resource is available only with Grafana Enterprise 7.+.
 * 
 * * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/create-reports/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/reporting/)
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.grafana.Dashboard;
 * import com.pulumi.grafana.DashboardArgs;
 * import com.pulumi.grafana.Report;
 * import com.pulumi.grafana.ReportArgs;
 * import com.pulumi.grafana.inputs.ReportScheduleArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var testDashboard = new Dashboard(&#34;testDashboard&#34;, DashboardArgs.builder()        
 *             .configJson(&#34;&#34;&#34;
 * {
 *   &#34;title&#34;: &#34;Dashboard for report&#34;,
 *   &#34;uid&#34;: &#34;report&#34;
 * }
 *             &#34;&#34;&#34;)
 *             .message(&#34;inital commit.&#34;)
 *             .build());
 * 
 *         var testReport = new Report(&#34;testReport&#34;, ReportArgs.builder()        
 *             .dashboardUid(testDashboard.uid())
 *             .recipients(&#34;some@email.com&#34;)
 *             .schedule(ReportScheduleArgs.builder()
 *                 .frequency(&#34;hourly&#34;)
 *                 .build())
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 */
@ResourceType(type="grafana:index/report:Report")
public class Report extends com.pulumi.resources.CustomResource {
    /**
     * Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
     * 
     * @deprecated
     * Use dashboard_uid instead
     * 
     */
    @Deprecated /* Use dashboard_uid instead */
    @Export(name="dashboardId", refs={Integer.class}, tree="[0]")
    private Output<Integer> dashboardId;

    /**
     * @return Dashboard to be sent in the report. This field is deprecated, use `dashboard_uid` instead.
     * 
     */
    public Output<Integer> dashboardId() {
        return this.dashboardId;
    }
    /**
     * Dashboard to be sent in the report.
     * 
     */
    @Export(name="dashboardUid", refs={String.class}, tree="[0]")
    private Output<String> dashboardUid;

    /**
     * @return Dashboard to be sent in the report.
     * 
     */
    public Output<String> dashboardUid() {
        return this.dashboardUid;
    }
    /**
     * Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
     * 
     */
    @Export(name="formats", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> formats;

    /**
     * @return Specifies what kind of attachment to generate for the report. Allowed values: `pdf`, `csv`, `image`.
     * 
     */
    public Output<Optional<List<String>>> formats() {
        return Codegen.optional(this.formats);
    }
    /**
     * Whether to include a link to the dashboard in the report. Defaults to `true`.
     * 
     */
    @Export(name="includeDashboardLink", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> includeDashboardLink;

    /**
     * @return Whether to include a link to the dashboard in the report. Defaults to `true`.
     * 
     */
    public Output<Optional<Boolean>> includeDashboardLink() {
        return Codegen.optional(this.includeDashboardLink);
    }
    /**
     * Whether to include a CSV file of table panel data. Defaults to `false`.
     * 
     */
    @Export(name="includeTableCsv", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> includeTableCsv;

    /**
     * @return Whether to include a CSV file of table panel data. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> includeTableCsv() {
        return Codegen.optional(this.includeTableCsv);
    }
    /**
     * Layout of the report. Allowed values: `simple`, `grid`. Defaults to `grid`.
     * 
     */
    @Export(name="layout", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> layout;

    /**
     * @return Layout of the report. Allowed values: `simple`, `grid`. Defaults to `grid`.
     * 
     */
    public Output<Optional<String>> layout() {
        return Codegen.optional(this.layout);
    }
    /**
     * Message to be sent in the report.
     * 
     */
    @Export(name="message", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> message;

    /**
     * @return Message to be sent in the report.
     * 
     */
    public Output<Optional<String>> message() {
        return Codegen.optional(this.message);
    }
    /**
     * Name of the report.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return Name of the report.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    @Export(name="orgId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> orgId;

    /**
     * @return The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    public Output<Optional<String>> orgId() {
        return Codegen.optional(this.orgId);
    }
    /**
     * Orientation of the report. Allowed values: `landscape`, `portrait`. Defaults to `landscape`.
     * 
     */
    @Export(name="orientation", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> orientation;

    /**
     * @return Orientation of the report. Allowed values: `landscape`, `portrait`. Defaults to `landscape`.
     * 
     */
    public Output<Optional<String>> orientation() {
        return Codegen.optional(this.orientation);
    }
    /**
     * List of recipients of the report.
     * 
     */
    @Export(name="recipients", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> recipients;

    /**
     * @return List of recipients of the report.
     * 
     */
    public Output<List<String>> recipients() {
        return this.recipients;
    }
    /**
     * Reply-to email address of the report.
     * 
     */
    @Export(name="replyTo", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> replyTo;

    /**
     * @return Reply-to email address of the report.
     * 
     */
    public Output<Optional<String>> replyTo() {
        return Codegen.optional(this.replyTo);
    }
    /**
     * Schedule of the report.
     * 
     */
    @Export(name="schedule", refs={ReportSchedule.class}, tree="[0]")
    private Output<ReportSchedule> schedule;

    /**
     * @return Schedule of the report.
     * 
     */
    public Output<ReportSchedule> schedule() {
        return this.schedule;
    }
    /**
     * Time range of the report.
     * 
     */
    @Export(name="timeRange", refs={ReportTimeRange.class}, tree="[0]")
    private Output</* @Nullable */ ReportTimeRange> timeRange;

    /**
     * @return Time range of the report.
     * 
     */
    public Output<Optional<ReportTimeRange>> timeRange() {
        return Codegen.optional(this.timeRange);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Report(String name) {
        this(name, ReportArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Report(String name, ReportArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Report(String name, ReportArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/report:Report", name, args == null ? ReportArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Report(String name, Output<String> id, @Nullable ReportState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/report:Report", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Report get(String name, Output<String> id, @Nullable ReportState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Report(name, id, state, options);
    }
}
