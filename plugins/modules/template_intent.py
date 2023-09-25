#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Ansible module to perform operations on project and templates in DNAC."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Madhan Sankaranarayanan, Rishita Chowdhary']

DOCUMENTATION = r"""
---
module: template_intent
short_description: Resource module for Template functions
description:
- Manage operations create, update and delete of the resource Configuration Template.
- API to create a template by project name and template name.
- API to update a template by template name and project name.
- API to delete a template by template name and project name.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of templates being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      author:
        description: Author of template.
        type: str
      composite:
        description: Is it composite template.
        type: bool
      containingTemplates:
        description: Configuration Template Create's containingTemplates.
        suboptions:
          composite:
            description: Is it composite template.
            type: bool
          description:
            description: Description of template.
            type: str
          deviceTypes:
            description: deviceTypes on which templates would be applied.
            type: list
            elements: dict
            suboptions:
              productFamily:
                description: Device family.
                type: str
              productSeries:
                description: Device series.
                type: str
              productType:
                description: Device type.
                type: str
          id:
            description: UUID of template.
            type: str
          language:
            description: Template language
            choices:
              - JINJA
              - VELOCITY
            type: str
          name:
            description: Name of template.
            type: str
          projectName:
            description: Name of the project under which templates are managed.
            type: str
            required: true
          projectDescription:
            description: Description of the project created.
            type: str
          rollbackTemplateParams:
            description: Params required for template rollback.
            type: list
            elements: dict
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                type: list
                elements: dict
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                    elements: str
                    type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
          tags:
            description: Configuration Template Create's tags.
            suboptions:
              id:
                description: UUID of tag.
                type: str
              name:
                description: Name of tag.
                type: str
            type: list
            elements: dict
          templateContent:
            description: Template content.
            type: str
          templateParams:
            description: Configuration Template Create's templateParams.
            elements: dict
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
                type: list
                elements: dict
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                    elements: str
                    type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
            type: list
          version:
            description: Current version of template.
            type: str
        type: list
        elements: dict
      createTime:
        description: Create time of template.
        type: int
      customParamsOrder:
        description: Custom Params Order.
        type: bool
      template_description:
        description: Description of template.
        type: str
      deviceTypes:
        description: Configuration Template Create's deviceTypes. This field is mandatory to create a new template.
        suboptions:
          productFamily:
            description: Device family.
            type: str
          productSeries:
            description: Device series.
            type: str
          productType:
            description: Device type.
            type: str
        type: list
        elements: dict
      failurePolicy:
        description: Define failure policy if template provisioning fails.
        type: str
      language:
        description: Template language
        choices:
          - JINJA
          - VELOCITY
        type: str
      lastUpdateTime:
        description: Update time of template.
        type: int
      latestVersionTime:
        description: Latest versioned template time.
        type: int
      templateName:
        description: Name of template. This field is mandatory to create a new template.
        type: str
      parentTemplateId:
        description: Parent templateID.
        type: str
      projectId:
        description: Project UUID.
        type: str
      projectName:
        description: Project name.
        type: str
      projectDescription:
        description: Project Description.
        type: str
      rollbackTemplateContent:
        description: Rollback template content.
        type: str
      rollbackTemplateParams:
        description: Configuration Template Create's rollbackTemplateParams.
        suboptions:
          binding:
            description: Bind to source.
            type: str
          customOrder:
            description: CustomOrder of template param.
            type: int
          dataType:
            description: Datatype of template param.
            type: str
          defaultValue:
            description: Default value of template param.
            type: str
          description:
            description: Description of template param.
            type: str
          displayName:
            description: Display name of param.
            type: str
          group:
            description: Group.
            type: str
          id:
            description: UUID of template param.
            type: str
          instructionText:
            description: Instruction text for param.
            type: str
          key:
            description: Key.
            type: str
          notParam:
            description: Is it not a variable.
            type: bool
          order:
            description: Order of template param.
            type: int
          paramArray:
            description: Is it an array.
            type: bool
          parameterName:
            description: Name of template param.
            type: str
          provider:
            description: Provider.
            type: str
          range:
            description: Configuration Template Create's range.
            suboptions:
              id:
                description: UUID of range.
                type: str
              maxValue:
                description: Max value of range.
                type: int
              minValue:
                description: Min value of range.
                type: int
            type: list
            elements: dict
          required:
            description: Is param required.
            type: bool
          selection:
            description: Configuration Template Create's selection.
            suboptions:
              defaultSelectedValues:
                description: Default selection values.
                elements: str
                type: list
              id:
                description: UUID of selection.
                type: str
              selectionType:
                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                type: str
              selectionValues:
                description: Selection values.
                type: dict
            type: dict
        type: list
        elements: dict
      softwareType:
        description: Applicable device software type. This field is mandatory to create a new template.
        type: str
      softwareVariant:
        description: Applicable device software variant.
        type: str
      softwareVersion:
        description: Applicable device software version.
        type: str
      template_tag:
        description: Configuration Template Create's tags.
        suboptions:
          id:
            description: UUID of tag.
            type: str
          name:
            description: Name of tag.
            type: str
        type: list
        elements: dict
      templateContent:
        description: Template content.
        type: str
      templateParams:
        description: Configuration Template Create's templateParams.
        suboptions:
          binding:
            description: Bind to source.
            type: str
          customOrder:
            description: CustomOrder of template param.
            type: int
          dataType:
            description: Datatype of template param.
            type: str
          defaultValue:
            description: Default value of template param.
            type: str
          description:
            description: Description of template param.
            type: str
          displayName:
            description: Display name of param.
            type: str
          group:
            description: Group.
            type: str
          id:
            description: UUID of template param.
            type: str
          instructionText:
            description: Instruction text for param.
            type: str
          key:
            description: Key.
            type: str
          notParam:
            description: Is it not a variable.
            type: bool
          order:
            description: Order of template param.
            type: int
          paramArray:
            description: Is it an array.
            type: bool
          parameterName:
            description: Name of template param.
            type: str
          provider:
            description: Provider.
            type: str
          range:
            description: Configuration Template Create's range.
            suboptions:
              id:
                description: UUID of range.
                type: str
              maxValue:
                description: Max value of range.
                type: int
              minValue:
                description: Min value of range.
                type: int
            type: list
            elements: dict
          required:
            description: Is param required.
            type: bool
          selection:
            description: Configuration Template Create's selection.
            suboptions:
              defaultSelectedValues:
                description: Default selection values.
                elements: str
                type: list
              id:
                description: UUID of selection.
                type: str
              selectionType:
                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                type: str
              selectionValues:
                description: Selection values.
                type: dict
            type: dict
        type: list
        elements: dict
      validationErrors:
        description: Configuration Template Create's validationErrors.
        suboptions:
          rollbackTemplateErrors:
            description: Validation or design conflicts errors of rollback template.
            elements: dict
            type: list
          templateErrors:
            description: Validation or design conflicts errors.
            elements: dict
            type: list
          templateId:
            description: UUID of template.
            type: str
          templateVersion:
            description: Current version of template.
            type: str
        type: dict
      version:
        description: Current version of template.
        type: str
      versionDescription:
        description: Template version comments.
        type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template,
    configuration_templates.ConfigurationTemplates.deletes_the_template,
    configuration_templates.ConfigurationTemplates.update_template,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/project/{projectId}/template,
    delete /dna/intent/api/v1/template-programmer/template/{templateId},
    put /dna/intent/api/v1/template-programmer/template,

"""

EXAMPLES = r"""
- name: Create a new template
  cisco.dnac.template_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        author: string
        composite: true
        createTime: 0
        customParamsOrder: true
        description: string
        deviceTypes:
        - productFamily: string
          productSeries: string
          productType: string
        failurePolicy: string
        id: string
        language: string
        lastUpdateTime: 0
        latestVersionTime: 0
        name: string
        parentTemplateId: string
        projectId: string
        projectName: string
        projectDescription: string
        rollbackTemplateContent: string
        softwareType: string
        softwareVariant: string
        softwareVersion: string
        tags:
        - id: string
          name: string
        templateContent: string
        validationErrors:
            rollbackTemplateErrors:
            - {}
            templateErrors:
            - {}
            templateId: string
            templateVersion: string
        version: string

"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of template/project
response_1:
  description: A dictionary with versioning details of the template as returned by the DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
                        "endTime": 0,
                        "version": 0,
                        "data": String,
                        "startTime": 0,
                        "username": String,
                        "progress": String,
                        "serviceType": String, "rootId": String,
                        "isError": bool,
                        "instanceTenantId": String,
                        "id": String
                        "version": 0
                  },
      "msg": String
    }

# Case_2: Error while deleting a template or when given project is not found
response_2:
  description: A list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

# Case_3: Given template already exists and requires no update
response_3:
  description: A dictionary with the exisiting template deatails as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "msg": String
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class DnacTemplate(DnacBase):
    """Class containing member attributes for template intent module"""
    def __init__(self, module):
        super().__init__(module)
        self.have_create_project = {}
        self.have_create_template = {}
        self.accepted_languages = ["JINJA", "VELOCITY"]

    def validate_input(self):
        """Validate the fields provided in the playbook"""

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = {'tags': {'type': 'list'},
                     'author': {'type': 'str'},
                     'composite': {'type': 'bool'},
                     'containingTemplates': {'type': 'list'},
                     'createTime': {'type': 'int'},
                     'customParamsOrder': {'type': 'bool'},
                     'description': {'type': 'str'},
                     'deviceTypes': {'type': 'list', 'elements': 'dict'},
                     'failurePolicy': {'type': 'str'},
                     'id': {'type': 'str'},
                     'language': {'type': 'str'},
                     'lastUpdateTime': {'type': 'int'},
                     'latestVersionTime': {'type': 'int'},
                     'name': {'type': 'str'},
                     'parentTemplateId': {'type': 'str'},
                     'projectId': {'type': 'str'},
                     'projectName': {'required': True, 'type': 'str'},
                     'projectDescription': {'type': 'str'},
                     'rollbackTemplateContent': {'type': 'str'},
                     'rollbackTemplateParams': {'type': 'list'},
                     'softwareType': {'type': 'str'},
                     'softwareVariant': {'type': 'str'},
                     'softwareVersion': {'type': 'str'},
                     'templateContent': {'type': 'str'},
                     'templateParams': {'type': 'list'},
                     'templateName': {'type': 'str'},
                     'validationErrors': {'type': 'dict'},
                     'version': {'type': 'str'},
                     'versionDescription': {'type': 'str'}
                     }
        # Validate template params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_project_params(self, params):
        """Store project parameters from the playbook for template processing in DNAC"""

        project_params = {"name": params.get("projectName"),
                          "description": params.get("projectDescription")
                          }
        return project_params

    def get_template_params(self, params):
        """Store template parameters from the playbook for template processing in DNAC"""

        temp_params = {
            "tags": params.get("template_tag"),
            "author": params.get("author"),
            "composite": params.get("composite"),
            "containingTemplates": params.get("containingTemplates"),
            "createTime": params.get("createTime"),
            "customParamsOrder": params.get("customParamsOrder"),
            "description": params.get("template_description"),
            "deviceTypes": params.get("deviceTypes"),
            "failurePolicy": params.get("failurePolicy"),
            "id": params.get("templateId"),
            "language": params.get("language").upper(),
            "lastUpdateTime": params.get("lastUpdateTime"),
            "latestVersionTime": params.get("latestVersionTime"),
            "name": params.get("templateName"),
            "parentTemplateId": params.get("parentTemplateId"),
            "projectId": params.get("projectId"),
            "projectName": params.get("projectName"),
            "rollbackTemplateContent": params.get("rollbackTemplateContent"),
            "rollbackTemplateParams": params.get("rollbackTemplateParams"),
            "softwareType": params.get("softwareType"),
            "softwareVariant": params.get("softwareVariant"),
            "softwareVersion": params.get("softwareVersion"),
            "templateContent": params.get("templateContent"),
            "templateParams": params.get("templateParams"),
            "validationErrors": params.get("validationErrors"),
            "version": params.get("version"),
            "project_id": params.get("projectId"),
        }
        return temp_params

    def get_template(self, config):
        """Get the template needed for updation or creation"""

        result = None
        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function="get_template_details",
            params={"template_id": config.get("templateId")}
        )
        if items:
            result = items

        self.log(str(items))
        self.result['response'] = items
        return result

    def get_have_project(self, config):
        """Get the current project related information from DNAC"""

        have_create_project = {}
        given_project_name = config.get("projectName")
        template_available = None

        # Check if project exists.
        project_details = self.get_project_details(given_project_name)
        # DNAC returns project details even if the substring matches.
        # Hence check the projectName retrieved from DNAC.
        if not (project_details and isinstance(project_details, list)):
            self.log("Project: {0} not found, need to create new project in DNAC".format(given_project_name))
            return None

        fetched_project_name = project_details[0].get('name')
        if fetched_project_name != given_project_name:
            self.log("Project {0} provided is not exact match in DNAC DB".format(given_project_name))
            return None

        template_available = project_details[0].get('templates')
        have_create_project["project_found"] = True
        have_create_project["id"] = project_details[0].get("id")
        have_create_project["isDeletable"] = project_details[0].get("isDeletable")

        self.have_create_project = have_create_project
        return template_available

    def get_have_template(self, config, template_available):
        """Get the current template related information from DNAC"""

        project_name = config.get("projectName")
        template_name = config.get("templateName")
        template = None
        have_create_template = {}

        have_create_template["isCommitPending"] = False
        have_create_template["template_found"] = False

        template_details = get_dict_result(template_available,
                                           "name",
                                           template_name)
        # Check if specified template in playbook is available
        if not template_details:
            self.log("Template {0} not found in project {1}".format(template_name, project_name))
            self.msg = "Template : {0} missing, new template to be created".format(template_name)
            self.status = "success"
            return self

        config["templateId"] = template_details.get("id")
        have_create_template["id"] = template_details.get("id")
        # Get available templates which are committed under the project
        template_list = self.dnac_apply['exec'](
            family="configuration_templates",
            function="gets_the_templates_available",
            params={"project_names": config.get("projectName")},
        )
        have_create_template["isCommitPending"] = True
        # This check will fail if specified template is there not committed in dnac
        if template_list and isinstance(template_list, list):
            template_info = get_dict_result(template_list,
                                            "name",
                                            template_name)
            if template_info:
                template = self.get_template(config)
                have_create_template["template"] = template
                have_create_template["isCommitPending"] = False
                have_create_template["template_found"] = template is not None \
                    and isinstance(template, dict)
                self.log("Template {0} is found and template "
                         "details are :{1}".format(template_name, str(template)))

        # There are committed templates in the project but the
        # one specified in the playbook may not be committed
        self.log("Commit pending for template name {0}"
                 " is {1}".format(template_name, have_create_template.get('isCommitPending')))

        self.have_create_template = have_create_template
        self.msg = "Successfully collected all template parameters from dnac for comparison"
        self.status = "success"
        return self

    def get_have(self, config):
        """Get the current project and template details from DNAC"""

        template_available = self.get_have_project(config)
        if template_available:
            self.get_have_template(config, template_available)

        self.msg = "Successfully collected all project and template \
                    parameters from dnac for comparison"
        self.status = "success"
        return self

    def get_project_details(self, project_name):
        """Get the details of specific project name provided"""

        items = self.dnac_apply['exec'](
            family="configuration_templates",
            function='get_projects',
            op_modifies=True,
            params={"name": project_name},
        )
        return items

    def get_want(self, config):
        """Get all the template and project related information from playbook
        that is needed to be created in DNAC"""

        want_create = {}
        template_params = self.get_template_params(config)
        project_params = self.get_project_params(config)
        version_comments = config.get("versionDescription")

        if self.params.get("state") == "merged":
            self.update_mandatory_parameters(template_params)

        want_create["template_params"] = template_params
        want_create["project_params"] = project_params
        want_create["comments"] = version_comments

        self.want_create = want_create
        self.msg = "Successfully collected all parameters from playbook " + \
                   "for comparison"
        self.status = "success"
        return self

    def create_project_or_template(self, is_create_project=False):
        """Call DNAC API to create project or template based on the input provided"""

        creation_id = None
        created = False
        template_params = self.want_create.get("template_params")
        project_params = self.want_create.get("project_params")

        if is_create_project:
            params_key = project_params
            name = "project: {0}".format(project_params.get('name'))
            validation_string = "Successfully created project"
            creation_value = "create_project"
        else:
            params_key = template_params
            name = "template: {0}".format(template_params.get('name'))
            validation_string = "Successfully created template"
            creation_value = "create_template"

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=creation_value,
            op_modifies=True,
            params=params_key,
        )
        if not isinstance(response, dict):
            self.log("Response not in dictionary format.")
            return creation_id, created

        task_id = response.get("response").get("taskId")
        if not task_id:
            self.log("Task id {0} not found".format(task_id))
            return creation_id, created

        while not created:
            task_details = self.get_task_details(task_id)
            if not task_details:
                self.log("Failed to get task details for taskid: {0}".format(task_id))
                return creation_id, created

            self.log("task_details: {0}".format(task_details))
            if task_details.get("isError"):
                self.log("isError set to true for taskid: {0}".format(task_id))
                return creation_id, created

            if validation_string not in task_details.get("progress"):
                self.log("progress set to {0} "
                         "for taskid: {1}".format(task_details.get('progress'), task_id))
                continue

            creation_id = task_details.get("data")
            if not creation_id:
                self.log("data is not found for taskid: {0}".format(task_id))
                continue

            created = True
            if is_create_project:
                # ProjectId is required for creating a new template.
                # Store it with other template parameters.
                template_params["projectId"] = creation_id
                template_params["project_id"] = creation_id

        self.log("New {0} created with id {1}".format(name, creation_id))
        return creation_id, created

    def requires_update(self):
        """Check if the template config given requires update."""

        if self.have_create_template.get("isCommitPending"):
            self.log("Template is in saved state and needs to be updated and committed")
            return True

        current_obj = self.have_create_template.get("template")
        requested_obj = self.want_create.get("template_params")
        obj_params = [
            ("tags", "tags", ""),
            ("author", "author", ""),
            ("composite", "composite", False),
            ("containingTemplates", "containingTemplates", []),
            ("createTime", "createTime", ""),
            ("customParamsOrder", "customParamsOrder", False),
            ("description", "description", ""),
            ("deviceTypes", "deviceTypes", []),
            ("failurePolicy", "failurePolicy", ""),
            ("id", "id", ""),
            ("language", "language", "VELOCITY"),
            ("lastUpdateTime", "lastUpdateTime", ""),
            ("latestVersionTime", "latestVersionTime", ""),
            ("name", "name", ""),
            ("parentTemplateId", "parentTemplateId", ""),
            ("projectId", "projectId", ""),
            ("projectName", "projectName", ""),
            ("rollbackTemplateContent", "rollbackTemplateContent", ""),
            ("rollbackTemplateParams", "rollbackTemplateParams", []),
            ("softwareType", "softwareType", ""),
            ("softwareVariant", "softwareVariant", ""),
            ("softwareVersion", "softwareVersion", ""),
            ("templateContent", "templateContent", ""),
            ("templateParams", "templateParams", []),
            ("validationErrors", "validationErrors", {}),
            ("version", "version", ""),
        ]

        return any(not dnac_compare_equality(current_obj.get(dnac_param, default),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param, default) in obj_params)

    def update_mandatory_parameters(self, template_params):
        """Update parameters which are mandatory for creating a template"""

        # Mandate fields required for creating a new template.
        # Store it with other template parameters.
        template_params["projectId"] = self.have_create_project.get("id")
        template_params["project_id"] = self.have_create_project.get("id")
        # Update language,deviceTypes and softwareType if not provided for existing template.
        if not template_params.get("language"):
            template_params["language"] = self.have_create_template.get('template') \
                .get('language')
        if not template_params.get("deviceTypes"):
            template_params["deviceTypes"] = self.have_create_template.get('template') \
                .get('deviceTypes')
        if not template_params.get("softwareType"):
            template_params["softwareType"] = self.have_create_template.get('template') \
                .get('softwareType')

    def validate_input_merge(self, template_exists):
        """Validate input after getting all the parameters from DNAC.
        "If mandate like deviceTypes, softwareType and language "
        "already present in DNAC for a template."
        "It is not required to be provided in playbook, "
        "but if it is new creation error will be thrown to provide these fields."""

        template_params = self.want_create.get("template_params")
        language = template_params.get("language").upper()
        if language:
            if language not in self.accepted_languages:
                self.msg = "Invalid value language {0} ." \
                           "Accepted language values are {1}" \
                           .format(self.accepted_languages, language)
                self.status = "failed"
                return self
        else:
            template_params["language"] = "JINJA"

        if not template_exists:
            if not template_params.get("deviceTypes") \
               or not template_params.get("softwareType"):
                self.msg = "DeviceTypes and SoftwareType are required arguments to create Templates"
                self.status = "failed"
                return self

        self.msg = "Input validated for merging"
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """Update/Create templates and projects in DNAC with fields provided in DNAC"""

        is_project_found = self.have_create_project.get("project_found")
        if not is_project_found:
            project_id, project_created = self.create_project_or_template(is_create_project=True)
            if project_created:
                self.log("project created with projectId : {0}".format(project_id))
            else:
                self.status = "failed"
                self.msg = "Project creation failed"
                return self

        is_template_found = self.have_create_template.get("template_found")
        template_params = self.want_create.get("template_params")
        template_id = None
        template_updated = False
        self.validate_input_merge(is_template_found).check_return_status()
        if is_template_found:
            if self.requires_update():
                response = self.dnac_apply['exec'](
                    family="configuration_templates",
                    function="update_template",
                    params=template_params,
                    op_modifies=True,
                )
                template_updated = True
                template_id = self.have_create_template.get("id")
                self.log("Updating Existing Template")
            else:
                # Template does not need update
                self.result['response'] = self.have_create_template.get("template")
                self.result['msg'] = "Template does not need update"
                self.status = "exited"
                return self
        else:
            if template_params.get("name"):
                template_id, template_updated = self.create_project_or_template()
            else:
                self.msg = "missing required arguments: TemplateName"
                self.status = "failed"
                return self

        if template_updated:
            # Template needs to be versioned
            version_params = {
                "comments": self.want_create.get("comments"),
                "templateId": template_id
            }
            response = self.dnac_apply['exec'](
                family="configuration_templates",
                function="version_template",
                op_modifies=True,
                params=version_params
            )
            task_details = {}
            task_id = response.get("response").get("taskId")
            if not task_id:
                self.msg = "Task id: {0} not found".format(task_id)
                self.status = "failed"
                return self
            task_details = self.get_task_details(task_id)
            self.result['changed'] = True
            self.result['msg'] = task_details.get('progress')
            self.result['diff'] = config
            self.log(str(task_details))
            self.result['response'] = task_details if task_details else response

            if not self.result.get('msg'):
                self.msg = "Error while versioning the template"
                self.status = "failed"
                return self

        self.msg = "Successfully completed merged state execution"
        self.status = "success"
        return self

    def delete_project_or_template(self, config, is_delete_project=False):
        """Call DNAC API to delete project or template with provided inputs"""

        if is_delete_project:
            params_key = {"project_id": self.have_create_project.get("id")}
            deletion_value = "deletes_the_project"
            name = "project: {0}".format(config.get('projectName'))
        else:
            template_params = self.want_create.get("template_params")
            params_key = {"template_id": self.have_create_template.get("id")}
            deletion_value = "deletes_the_template"
            name = "templateName: {0}".format(template_params.get('templateName'))

        response = self.dnac_apply['exec'](
            family="configuration_templates",
            function=deletion_value,
            params=params_key,
        )
        task_id = response.get("response").get("taskId")
        if task_id:
            task_details = self.get_task_details(task_id)
            self.result['changed'] = True
            self.result['msg'] = task_details.get('progress')
            self.result['diff'] = config

            self.log(str(task_details))
            self.result['response'] = task_details if task_details else response
            if not self.result['msg']:
                self.result['msg'] = "Error while deleting {name} : "
                self.status = "failed"
                return self

        self.msg = "Successfully deleted {0} ".format(name)
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """Delete projects or templates in DNAC with fields provided in playbook."""

        is_project_found = self.have_create_project.get("project_found")
        projectName = config.get("projectName")

        if not is_project_found:
            self.msg = "Project {0} is not found".format(projectName)
            self.status = "failed"
            return self

        is_template_found = self.have_create_template.get("template_found")
        template_params = self.want_create.get("template_params")
        template_name = config.get("templateName")
        if template_params.get("name"):
            if is_template_found:
                self.delete_project_or_template(config)
            else:
                self.msg = "Invalid template {0} under project".format(template_name)
                self.status = "failed"
                return self
        else:
            self.log("Template Name is empty, deleting the project and its associated templates")
            is_project_deletable = self.have_create_project.get("isDeletable")
            if is_project_deletable:
                self.delete_project_or_template(config, is_delete_project=True)
            else:
                self.msg = "Project is not deletable"
                self.status = "failed"
                return self

        self.msg = "Successfully completed delete state execution"
        self.status = "success"
        return self

    def reset_values(self):
        """Reset all neccessary attributes to default values"""

        self.have_create_project.clear()
        self.have_create_template.clear()
        self.want_create.clear()


def main():
    """ main entry point for module execution"""

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    dnac_template = DnacTemplate(module)
    dnac_template.validate_input().check_return_status()
    state = dnac_template.params.get("state")
    if state not in dnac_template.supported_states:
        dnac_template.status = "invalid"
        dnac_template.msg = "State {0} is invalid".format(state)
        dnac_template.check_return_status()

    for config in dnac_template.validated_config:
        dnac_template.reset_values()
        dnac_template.get_have(config).check_return_status()
        dnac_template.get_want(config).check_return_status()
        dnac_template.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_template.result)


if __name__ == '__main__':
    main()
