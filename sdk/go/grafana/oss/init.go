// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package oss

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "grafana:oss/annotation:Annotation":
		r = &Annotation{}
	case "grafana:oss/apiKey:ApiKey":
		r = &ApiKey{}
	case "grafana:oss/dashboard:Dashboard":
		r = &Dashboard{}
	case "grafana:oss/dashboardPermission:DashboardPermission":
		r = &DashboardPermission{}
	case "grafana:oss/dashboardPermissionItem:DashboardPermissionItem":
		r = &DashboardPermissionItem{}
	case "grafana:oss/dashboardPublic:DashboardPublic":
		r = &DashboardPublic{}
	case "grafana:oss/dataSource:DataSource":
		r = &DataSource{}
	case "grafana:oss/dataSourceConfig:DataSourceConfig":
		r = &DataSourceConfig{}
	case "grafana:oss/folder:Folder":
		r = &Folder{}
	case "grafana:oss/folderPermission:FolderPermission":
		r = &FolderPermission{}
	case "grafana:oss/folderPermissionItem:FolderPermissionItem":
		r = &FolderPermissionItem{}
	case "grafana:oss/libraryPanel:LibraryPanel":
		r = &LibraryPanel{}
	case "grafana:oss/organization:Organization":
		r = &Organization{}
	case "grafana:oss/organizationPreferences:OrganizationPreferences":
		r = &OrganizationPreferences{}
	case "grafana:oss/playlist:Playlist":
		r = &Playlist{}
	case "grafana:oss/serviceAccount:ServiceAccount":
		r = &ServiceAccount{}
	case "grafana:oss/serviceAccountPermission:ServiceAccountPermission":
		r = &ServiceAccountPermission{}
	case "grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem":
		r = &ServiceAccountPermissionItem{}
	case "grafana:oss/serviceAccountToken:ServiceAccountToken":
		r = &ServiceAccountToken{}
	case "grafana:oss/ssoSettings:SsoSettings":
		r = &SsoSettings{}
	case "grafana:oss/team:Team":
		r = &Team{}
	case "grafana:oss/user:User":
		r = &User{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/annotation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/apiKey",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dashboard",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dashboardPermission",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dashboardPermissionItem",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dashboardPublic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dataSource",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/dataSourceConfig",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/folder",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/folderPermission",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/folderPermissionItem",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/libraryPanel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/organization",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/organizationPreferences",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/playlist",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/serviceAccount",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/serviceAccountPermission",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/serviceAccountPermissionItem",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/serviceAccountToken",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/ssoSettings",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/team",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"grafana",
		"oss/user",
		&module{version},
	)
}
