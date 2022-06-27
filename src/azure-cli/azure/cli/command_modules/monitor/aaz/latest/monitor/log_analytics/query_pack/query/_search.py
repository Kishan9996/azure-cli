# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor log-analytics query-pack query search",
    is_preview=True,
)
class Search(AAZCommand):
    """Search a list of queries defined within a log analytics query pack according to given search properties.

    :example: Search queries in a query pack
        az monitor log-analytics query-pack query search -g resourceGroupName --query-pack-name queryPackName --categories network --resource-types microsoft.insights/autoscalesettings --solutions networkmonitoring --tags version="[v2021-12-01]"

    :example: Search queries in a query pack without query body content
        az monitor log-analytics query-pack query search -g resourceGroupName --query-pack-name queryPackName --categories network --resource-types microsoft.insights/autoscalesettings --solutions networkmonitoring --tags version="[v2021-12-01]" --include-body false
    """

    _aaz_info = {
        "version": "2019-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/querypacks/{}/queries/search", "2019-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.query_pack_name = AAZStrArg(
            options=["--query-pack-name"],
            help="The name of the log analytics query pack.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.include_body = AAZBoolArg(
            options=["--include-body"],
            help="Whether or not to return the body of each applicable query. If false, only return the query information.  Default: true.",
        )

        # define Arg Group "SearchProperties"

        _args_schema = cls._args_schema
        _args_schema.categories = AAZListArg(
            options=["--categories"],
            arg_group="SearchProperties",
            help={"short-summary": "The related categories for the function.", "long-summary": "Supported value are: `security`, `network`, `management`, `virtualmachines`, `container`, `audit`, `desktopanalytics`, `workloads`, `resources`, `applications`, `monitor`, `databases`, `windowsvirtualdesktop` etc."},
        )
        _args_schema.resource_types = AAZListArg(
            options=["--resource-types"],
            arg_group="SearchProperties",
            help="The related resource types for the function.",
        )
        _args_schema.solutions = AAZListArg(
            options=["--solutions"],
            arg_group="SearchProperties",
            help="The related Log Analytics solutions for the function.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="SearchProperties",
            help="Tags associated with the query.",
        )

        categories = cls._args_schema.categories
        categories.Element = AAZStrArg()

        resource_types = cls._args_schema.resource_types
        resource_types.Element = AAZStrArg()

        solutions = cls._args_schema.solutions
        solutions.Element = AAZStrArg()

        tags = cls._args_schema.tags
        tags.Element = AAZListArg()

        _element = cls._args_schema.tags.Element
        _element.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.QueriesSearch(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class QueriesSearch(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/search",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "queryPackName", self.ctx.args.query_pack_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "includeBody", self.ctx.args.include_body,
                ),
                **self.serialize_query_param(
                    "api-version", "2019-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("related", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            related = _builder.get(".related")
            if related is not None:
                related.set_prop("categories", AAZListType, ".categories")
                related.set_prop("resourceTypes", AAZListType, ".resource_types")
                related.set_prop("solutions", AAZListType, ".solutions")

            categories = _builder.get(".related.categories")
            if categories is not None:
                categories.set_elements(AAZStrType, ".")

            resource_types = _builder.get(".related.resourceTypes")
            if resource_types is not None:
                resource_types.set_elements(AAZStrType, ".")

            solutions = _builder.get(".related.solutions")
            if solutions is not None:
                solutions.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZListType)

            _elements = _builder.get(".tags{}")
            if _elements is not None:
                _elements.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.author = AAZStrType(
                flags={"read_only": True},
            )
            properties.body = AAZStrType(
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.id = AAZStrType(
                flags={"read_only": True},
            )
            properties.related = AAZObjectType()
            properties.tags = AAZDictType()
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )
            properties.time_modified = AAZStrType(
                serialized_name="timeModified",
                flags={"read_only": True},
            )

            related = cls._schema_on_200.value.Element.properties.related
            related.categories = AAZListType()
            related.resource_types = AAZListType(
                serialized_name="resourceTypes",
            )
            related.solutions = AAZListType()

            categories = cls._schema_on_200.value.Element.properties.related.categories
            categories.Element = AAZStrType()

            resource_types = cls._schema_on_200.value.Element.properties.related.resource_types
            resource_types.Element = AAZStrType()

            solutions = cls._schema_on_200.value.Element.properties.related.solutions
            solutions.Element = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.tags
            tags.Element = AAZListType()

            _element = cls._schema_on_200.value.Element.properties.tags.Element
            _element.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            return cls._schema_on_200


__all__ = ["Search"]
