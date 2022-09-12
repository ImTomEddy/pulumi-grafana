// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Data source for retrieving sets of cloud IPs. See https://grafana.com/docs/grafana-cloud/reference/allow-list/ for more info
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := grafana.GetCloudIps(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetCloudIps(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetCloudIpsResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetCloudIpsResult
	err := ctx.Invoke("grafana:index/getCloudIps:getCloudIps", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getCloudIps.
type GetCloudIpsResult struct {
	// Set of IP addresses that are used for hosted alerts.
	HostedAlerts []string `pulumi:"hostedAlerts"`
	// Set of IP addresses that are used for hosted Grafana.
	HostedGrafanas []string `pulumi:"hostedGrafanas"`
	// Set of IP addresses that are used for hosted logs.
	HostedLogs []string `pulumi:"hostedLogs"`
	// Set of IP addresses that are used for hosted metrics.
	HostedMetrics []string `pulumi:"hostedMetrics"`
	// Set of IP addresses that are used for hosted traces.
	HostedTraces []string `pulumi:"hostedTraces"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}