// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

func LookupCloudStack(ctx *pulumi.Context, args *LookupCloudStackArgs, opts ...pulumi.InvokeOption) (*LookupCloudStackResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCloudStackResult
	err := ctx.Invoke("grafana:index/getCloudStack:getCloudStack", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCloudStack.
type LookupCloudStackArgs struct {
	Slug string `pulumi:"slug"`
}

// A collection of values returned by getCloudStack.
type LookupCloudStackResult struct {
	AlertmanagerName              string            `pulumi:"alertmanagerName"`
	AlertmanagerStatus            string            `pulumi:"alertmanagerStatus"`
	AlertmanagerUrl               string            `pulumi:"alertmanagerUrl"`
	AlertmanagerUserId            int               `pulumi:"alertmanagerUserId"`
	Description                   string            `pulumi:"description"`
	GraphiteName                  string            `pulumi:"graphiteName"`
	GraphiteStatus                string            `pulumi:"graphiteStatus"`
	GraphiteUrl                   string            `pulumi:"graphiteUrl"`
	GraphiteUserId                int               `pulumi:"graphiteUserId"`
	Id                            string            `pulumi:"id"`
	Labels                        map[string]string `pulumi:"labels"`
	LogsName                      string            `pulumi:"logsName"`
	LogsStatus                    string            `pulumi:"logsStatus"`
	LogsUrl                       string            `pulumi:"logsUrl"`
	LogsUserId                    int               `pulumi:"logsUserId"`
	Name                          string            `pulumi:"name"`
	OrgId                         int               `pulumi:"orgId"`
	OrgName                       string            `pulumi:"orgName"`
	OrgSlug                       string            `pulumi:"orgSlug"`
	OtlpUrl                       string            `pulumi:"otlpUrl"`
	ProfilesName                  string            `pulumi:"profilesName"`
	ProfilesStatus                string            `pulumi:"profilesStatus"`
	ProfilesUrl                   string            `pulumi:"profilesUrl"`
	ProfilesUserId                int               `pulumi:"profilesUserId"`
	PrometheusName                string            `pulumi:"prometheusName"`
	PrometheusRemoteEndpoint      string            `pulumi:"prometheusRemoteEndpoint"`
	PrometheusRemoteWriteEndpoint string            `pulumi:"prometheusRemoteWriteEndpoint"`
	PrometheusStatus              string            `pulumi:"prometheusStatus"`
	PrometheusUrl                 string            `pulumi:"prometheusUrl"`
	PrometheusUserId              int               `pulumi:"prometheusUserId"`
	RegionSlug                    string            `pulumi:"regionSlug"`
	Slug                          string            `pulumi:"slug"`
	Status                        string            `pulumi:"status"`
	TracesName                    string            `pulumi:"tracesName"`
	TracesStatus                  string            `pulumi:"tracesStatus"`
	TracesUrl                     string            `pulumi:"tracesUrl"`
	TracesUserId                  int               `pulumi:"tracesUserId"`
	Url                           string            `pulumi:"url"`
}

func LookupCloudStackOutput(ctx *pulumi.Context, args LookupCloudStackOutputArgs, opts ...pulumi.InvokeOption) LookupCloudStackResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCloudStackResult, error) {
			args := v.(LookupCloudStackArgs)
			r, err := LookupCloudStack(ctx, &args, opts...)
			var s LookupCloudStackResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCloudStackResultOutput)
}

// A collection of arguments for invoking getCloudStack.
type LookupCloudStackOutputArgs struct {
	Slug pulumi.StringInput `pulumi:"slug"`
}

func (LookupCloudStackOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCloudStackArgs)(nil)).Elem()
}

// A collection of values returned by getCloudStack.
type LookupCloudStackResultOutput struct{ *pulumi.OutputState }

func (LookupCloudStackResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCloudStackResult)(nil)).Elem()
}

func (o LookupCloudStackResultOutput) ToLookupCloudStackResultOutput() LookupCloudStackResultOutput {
	return o
}

func (o LookupCloudStackResultOutput) ToLookupCloudStackResultOutputWithContext(ctx context.Context) LookupCloudStackResultOutput {
	return o
}

func (o LookupCloudStackResultOutput) AlertmanagerName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.AlertmanagerName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) AlertmanagerStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.AlertmanagerStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) AlertmanagerUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.AlertmanagerUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) AlertmanagerUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.AlertmanagerUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) GraphiteName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.GraphiteName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) GraphiteStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.GraphiteStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) GraphiteUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.GraphiteUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) GraphiteUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.GraphiteUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupCloudStackResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

func (o LookupCloudStackResultOutput) LogsName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.LogsName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) LogsStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.LogsStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) LogsUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.LogsUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) LogsUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.LogsUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) OrgId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.OrgId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) OrgName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.OrgName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) OrgSlug() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.OrgSlug }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) OtlpUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.OtlpUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) ProfilesName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.ProfilesName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) ProfilesStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.ProfilesStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) ProfilesUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.ProfilesUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) ProfilesUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.ProfilesUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) PrometheusName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.PrometheusName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) PrometheusRemoteEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.PrometheusRemoteEndpoint }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) PrometheusRemoteWriteEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.PrometheusRemoteWriteEndpoint }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) PrometheusStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.PrometheusStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) PrometheusUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.PrometheusUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) PrometheusUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.PrometheusUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) RegionSlug() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.RegionSlug }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) Slug() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Slug }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Status }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) TracesName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.TracesName }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) TracesStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.TracesStatus }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) TracesUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.TracesUrl }).(pulumi.StringOutput)
}

func (o LookupCloudStackResultOutput) TracesUserId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupCloudStackResult) int { return v.TracesUserId }).(pulumi.IntOutput)
}

func (o LookupCloudStackResultOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCloudStackResult) string { return v.Url }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCloudStackResultOutput{})
}
