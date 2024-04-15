// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

func LookupOncallOutgoingWebhook(ctx *pulumi.Context, args *LookupOncallOutgoingWebhookArgs, opts ...pulumi.InvokeOption) (*LookupOncallOutgoingWebhookResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupOncallOutgoingWebhookResult
	err := ctx.Invoke("grafana:index/getOncallOutgoingWebhook:getOncallOutgoingWebhook", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOncallOutgoingWebhook.
type LookupOncallOutgoingWebhookArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getOncallOutgoingWebhook.
type LookupOncallOutgoingWebhookResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func LookupOncallOutgoingWebhookOutput(ctx *pulumi.Context, args LookupOncallOutgoingWebhookOutputArgs, opts ...pulumi.InvokeOption) LookupOncallOutgoingWebhookResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOncallOutgoingWebhookResult, error) {
			args := v.(LookupOncallOutgoingWebhookArgs)
			r, err := LookupOncallOutgoingWebhook(ctx, &args, opts...)
			var s LookupOncallOutgoingWebhookResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOncallOutgoingWebhookResultOutput)
}

// A collection of arguments for invoking getOncallOutgoingWebhook.
type LookupOncallOutgoingWebhookOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupOncallOutgoingWebhookOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOncallOutgoingWebhookArgs)(nil)).Elem()
}

// A collection of values returned by getOncallOutgoingWebhook.
type LookupOncallOutgoingWebhookResultOutput struct{ *pulumi.OutputState }

func (LookupOncallOutgoingWebhookResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOncallOutgoingWebhookResult)(nil)).Elem()
}

func (o LookupOncallOutgoingWebhookResultOutput) ToLookupOncallOutgoingWebhookResultOutput() LookupOncallOutgoingWebhookResultOutput {
	return o
}

func (o LookupOncallOutgoingWebhookResultOutput) ToLookupOncallOutgoingWebhookResultOutputWithContext(ctx context.Context) LookupOncallOutgoingWebhookResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o LookupOncallOutgoingWebhookResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOncallOutgoingWebhookResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupOncallOutgoingWebhookResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOncallOutgoingWebhookResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOncallOutgoingWebhookResultOutput{})
}
