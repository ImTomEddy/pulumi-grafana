// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/escalation_chains/)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := grafana.LookupOncallEscalationChain(ctx, &grafana.LookupOncallEscalationChainArgs{
//				Name: "default",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupOncallEscalationChain(ctx *pulumi.Context, args *LookupOncallEscalationChainArgs, opts ...pulumi.InvokeOption) (*LookupOncallEscalationChainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupOncallEscalationChainResult
	err := ctx.Invoke("grafana:index/getOncallEscalationChain:getOncallEscalationChain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOncallEscalationChain.
type LookupOncallEscalationChainArgs struct {
	// The escalation chain name.
	Name string `pulumi:"name"`
}

// A collection of values returned by getOncallEscalationChain.
type LookupOncallEscalationChainResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The escalation chain name.
	Name string `pulumi:"name"`
}

func LookupOncallEscalationChainOutput(ctx *pulumi.Context, args LookupOncallEscalationChainOutputArgs, opts ...pulumi.InvokeOption) LookupOncallEscalationChainResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOncallEscalationChainResult, error) {
			args := v.(LookupOncallEscalationChainArgs)
			r, err := LookupOncallEscalationChain(ctx, &args, opts...)
			var s LookupOncallEscalationChainResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOncallEscalationChainResultOutput)
}

// A collection of arguments for invoking getOncallEscalationChain.
type LookupOncallEscalationChainOutputArgs struct {
	// The escalation chain name.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupOncallEscalationChainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOncallEscalationChainArgs)(nil)).Elem()
}

// A collection of values returned by getOncallEscalationChain.
type LookupOncallEscalationChainResultOutput struct{ *pulumi.OutputState }

func (LookupOncallEscalationChainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOncallEscalationChainResult)(nil)).Elem()
}

func (o LookupOncallEscalationChainResultOutput) ToLookupOncallEscalationChainResultOutput() LookupOncallEscalationChainResultOutput {
	return o
}

func (o LookupOncallEscalationChainResultOutput) ToLookupOncallEscalationChainResultOutputWithContext(ctx context.Context) LookupOncallEscalationChainResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o LookupOncallEscalationChainResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOncallEscalationChainResult) string { return v.Id }).(pulumi.StringOutput)
}

// The escalation chain name.
func (o LookupOncallEscalationChainResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOncallEscalationChainResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOncallEscalationChainResultOutput{})
}
