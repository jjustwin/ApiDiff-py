apiInfo = [

    {

        "type": "get",

        "url": "/u/dental/connection/action/:tid/:taction",

        "title": "齿科关系网删除/接受/拒绝接口",

        "description": "<p>urlName: dentalConnectionAction</p>",

        "group": "dental/connection",

        "name": "dentalConnectionAction",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "tid",

                        "description": "<p>关系id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "taction",

                        "description": "<p>行为类型, delete/accept/refuse</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"xxx\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/connection.go",

        "groupTitle": "dental/connection"
    },

    {

        "type": "post",

        "url": "/u/dental/connection/add",

        "title": "齿科关系网添加接口",

        "description": "<p>urlName: dentalConnectionAdd</p>",

        "group": "dental/connection",

        "name": "dentalConnectionAdd",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "targetType",

                        "description": "<p>连接类型，user/lab</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "targetID",

                        "description": "<p>连接目标ID</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "userID",

                        "description": "<p>来源用户iD</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"targetType\":\"xxx\",\n\t \"targetID\":\"xxx\",\n\t \"userID\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"userID\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/connection.go",

        "groupTitle": "dental/connection"
    },

    {

        "type": "get",

        "url": "/u/dental/c/list",

        "title": "齿科机构成员接口",

        "description": "<p>urlName: dentalConnectionList</p>",

        "group": "dental/connection",

        "name": "dentalConnectionList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n\t\t\"page\": 1,\n\t\t\"pageSize\": 50,\n\t\t\"pages\": 1,\n\t\t\"total\": 6\n\t},\n  \t\"result\": [{\n\t\t\"hospitalID\": \"\",\n\t\t\"id\": \"1011e613-ffaf-5f12-bb2e-ec82b417dd0a\",\n\t\t\"status\": \"active\",\n\t\t\"targetLab\": \"南京市口腔修复工艺科\",\n\t\t\"targetLabAdmins\": \"125516d1-8b2f-50c9-a811-cfc51f73ad5f\",\n\t\t\"user\": \"喻茜茜\",\n\t\t\"userID\": \"902eb5ac-30c6-5767-903d-b7a352c13818\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/connection.go",

        "groupTitle": "dental/connection"
    },

    {

        "type": "get",

        "url": "/u/dental/dv/list",

        "title": "齿科机构成员接口",

        "description": "<p>urlName: dentalDeviceBind</p>",

        "group": "dental/device",

        "name": "dentalDeviceBind",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n\t\t\"page\": 1,\n\t\t\"pageSize\": 50,\n\t\t\"pages\": 1,\n\t\t\"total\": 6\n\t},\n  \t\"result\": [{\n\t\t\"CreateBy\": \"张海涛\",\n\t\t\"CreateOn\": \"2020-11-23T05:15:10Z\",\n\t\t\"FactoryAdmins\": \"\",\n\t\t\"ID\": \"50faa526-4345-5530-91fb-ce27b7db9b8d\",\n\t\t\"Lab\": \"深圳市完美义齿有限公司\",\n\t\t\"SN\": \"AOS-BX036L01\",\n\t\t\"UserID\": \"b8c5f467-3061-428b-826c-13fd035566d5\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/device.go",

        "groupTitle": "dental/device"
    },

    {

        "type": "post",

        "url": "/u/dental/device/delete/:tid",

        "title": "齿科设备绑定删除接口",

        "description": "<p>urlName: dentalDeviceDelete</p>",

        "group": "dental/device",

        "name": "dentalDeviceDelete",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"xxx\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/device.go",

        "groupTitle": "dental/device"
    },

    {

        "type": "post",

        "url": "/u/dental/dv/add",

        "title": "齿科设备绑定接口",

        "description": "<p>urlName: deviceBindAdd</p>",

        "group": "dental/device",

        "name": "deviceBindAdd",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"serialNum\": \"xxx\",\n\t\"labID\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"serialNum\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/device.go",

        "groupTitle": "dental/device"
    },

    {

        "type": "post",

        "url": "/fetchDL",

        "title": "齿科设备获取绑定信息接口",

        "description": "<p>urlName: fetchDeviceLab</p>",

        "group": "dental/device",

        "name": "fetchDeviceLab",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "modelCode",

                        "description": "<p>设备型号唯一名</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "serialNum",

                        "description": "<p>设备序列号且必须是入库记录中有的</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"modelCode\": \"xxx\",\n\t \"serialNum\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "fields": {

                "Success 200": [

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": True,

                        "field": "owner",

                        "description": "<p>设备归属的人或机构名称，有可能为空</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": True,

                        "field": "lab",

                        "description": "<p>设备指定的下单技工所名称，有可能为空</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": True,

                        "field": "labID",

                        "description": "<p>设备指定的下单技工所ID，有可能为空</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": True,

                        "field": "deviceExist",

                        "description": "<p>设备是否在库中存在</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\t\"deviceExist\":True,\n\t\t\"deviceActived\":True,\n\t\t\"owner\":\"xxx\",\n\t\t\"lab\":\"xxx\",\n\t\t\"labID\":\"xxx\"\n\t}\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/device.go",

        "groupTitle": "dental/device"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/options",

        "title": "齿科机构表单列表接口",

        "description": "<p>urlName: dentalFactory</p>",

        "group": "dental/institution",

        "name": "dentalFactory",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n  \t\"result\": [{\n\t\t\"KeyName\": \"xxx\",\n\t\t\"KeyValue\": \"xxx\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/add",

        "title": "齿科机构添加接口",

        "description": "<p>urlName: dentalFactoryAdd</p>",

        "group": "dental/institution",

        "name": "dentalFactoryAdd",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.change_dental_list\"]"
            }
        ],

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"name\": \"xxx\",\n\t\"factoryType\": \"xxx\",\n\t\"domain\": \"xxx\",\n\t\"addr\": \"xxx\",\n\t\"contact\": \"xxx\",\n\t\"contactWay\": \"xxx\",\n\t\"comments\": \"xxx\",\n\t\"parentID\": \"xxx\",\n\t\"status\": \"canceled\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"name\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/change",

        "title": "齿科机构修改接口",

        "description": "<p>urlName: dentalFactoryChange</p>",

        "group": "dental/institution",

        "name": "dentalFactoryChange",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.change_dental_list\"]"
            }
        ],

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"id\": \"xxx\",\n\t\"name\": \"xxx\",\n\t\"factoryType\": \"xxx\",\n\t\"domain\": \"xxx\",\n\t\"addr\": \"xxx\",\n\t\"contact\": \"xxx\",\n\t\"contactWay\": \"xxx\",\n\t\"comments\": \"xxx\",\n\t\"parentID\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"name\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/detail/:tid",

        "title": "齿科机构详情接口",

        "description": "<p>urlName: dentalFactoryDetail</p>",

        "group": "dental/institution",

        "name": "dentalFactoryDetail",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.manage_dental_member\", \"dental.manage_dental_device\", \"dental.change_dental_list\", \"dental.view_dental_list\"]"
            }
        ],

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"status\": \"xxx\",\n  \t\"result\": {\n\t\t\"id\": \"xxx\",\n\t\t\"createOn\": \"xxx\",\n\t\t\"createBy\": \"xxx\",\n\t\t\"changeOn\": \"xxx\",\n\t\t\"changeBy\": \"xxx\",\n\t\t\"name\": \"xxx\",\n\t\t\"factoryType\": \"xxx\",\n\t\t\"domain\": \"xxx\",\n\t\t\"fromDomain\": \"xxx\",\n\t\t\"addr\": \"xxx\",\n\t\t\"contact\": \"xxx\",\n\t\t\"contactWay\": \"xxx\",\n\t\t\"comments\": \"xxx\",\n\t\t\"hasEForm\": \"xxx\",\n\t\t\"parentID\": \"xxx\",\n\t\t\"members\": \"xxx\",\n\t\t\"status\": \"canceled\"\n    }\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/list",

        "title": "齿科机构列表接口",

        "description": "<p>urlName: dentalFactoryList</p>",

        "group": "dental/institution",

        "name": "dentalFactoryList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.view_dental_list\"]"
            }
        ],

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n\t\t\"page\": 1,\n\t\t\"pageSize\": 50,\n\t\t\"pages\": 1,\n\t\t\"total\": 6\n\t},\n  \t\"result\": [{\n\t\t\"id\": \"xxx\",\n\t\t\"createOn\": \"xxx\",\n\t\t\"createBy\": \"xxx\",\n\t\t\"changeOn\": \"xxx\",\n\t\t\"changeBy\": \"xxx\",\n\t\t\"name\": \"xxx\",\n\t\t\"factoryType\": \"xxx\",\n\t\t\"domain\": \"xxx\",\n\t\t\"fromDomain\": \"xxx\",\n\t\t\"addr\": \"xxx\",\n\t\t\"contact\": \"xxx\",\n\t\t\"contactWay\": \"xxx\",\n\t\t\"comments\": \"xxx\",\n\t\t\"hasEForm\": \"xxx\",\n\t\t\"parentID\": \"xxx\",\n\t\t\"members\": \"xxx\",\n\t\t\"status\": \"canceled\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/factory/setting",

        "title": "齿科机构设置接口",

        "description": "<p>urlName: dentalFactorySetting</p>",

        "group": "dental/institution",

        "name": "dentalFactorySetting",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"id\": \"xxx\",\n\t\"addr\": \"xxx\",\n\t\"contact\": \"xxx\",\n\t\"contactWay\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"addr\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "post",

        "url": "/u/dental/fetchlab",

        "title": "获取技工所列表接口",

        "description": "<p>urlName: dentalFetchLab 根据账号id及设备信息过滤</p>",

        "group": "dental/institution",

        "name": "dentalFetchLab",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "doctorId",

                        "description": "<p>是医生的用户id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "modelCode",

                        "description": "<p>Optional 设备型号唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "serialNum",

                        "description": "<p>Optional 设备序列号</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softName",

                        "description": "<p>软件名称唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softVer",

                        "description": "<p>软件版本，必须是1.0.0.0类似的格式，只允许.和数字</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueInstallCode",

                        "description": "<p>软件在客户端安装后的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueUsageCode",

                        "description": "<p>软件在客户端启动时的唯一id</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"doctorId\": \"xxxx\",\n\t \"client\": {\n\t\t \"modelCode\": \"xxx\",\n\t\t \"serialNum\": \"xxx\",\n\t\t \"softName\": \"xxx\",\n\t\t \"softVer\": \"1.0.0.0\",\n\t\t \"uniqueInstallCode\": \"xxx\",\n\t\t \"uniqueUsageCode\": \"xxx\"\n\t }\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": [{\n\t\t\"name\":\"xxx\",\n\t\t\"id\":\"xxx\"\n\t}]\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/institution"
    },

    {

        "type": "get",

        "url": "/u/dental/member/action/:tid/:tType",

        "title": "齿科机构成员行为处理接口",

        "description": "<p>urlName: actionDentalFactoryMember</p>",

        "group": "dental/member",

        "name": "actionDentalFactoryMember",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/member.go",

        "groupTitle": "dental/member"
    },

    {

        "type": "get",

        "url": "/u/dental/member/list",

        "title": "齿科机构成员接口",

        "description": "<p>urlName: dentalMember</p>",

        "group": "dental/member",

        "name": "dentalMember",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.view_dental_list\"]"
            }
        ],

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n\t\t\"page\": 1,\n\t\t\"pageSize\": 50,\n\t\t\"pages\": 1,\n\t\t\"total\": 6\n\t},\n  \t\"result\": [{\n\t\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\t\"IsAdmin\": \"y\",\n\t\t\"FactoryName\": \"cn\",\n\t\t\"FactoryID\": \"repair\",\n\t\t\"FactoryType\": \"xxxxxx\",\n\t\t\"UserID\": \"FDI\",\n\t\t\"NickName\": True,\n\t\t\"Email\": \"notes\",\n\t\t\"Phone\": \"patient_name\",\n\t\t\"PhoneArea\": \"canceled\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/member.go",

        "groupTitle": "dental/member"
    },

    {

        "type": "get",

        "url": "/u/dental/m/add",

        "title": "齿科机构成员添加接口",

        "description": "<p>urlName: dentalMemberAdd</p>",

        "group": "dental/member",

        "name": "dentalMemberAdd",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.admin_dental_member\", \"dental.manage_dental_member\"]"
            }
        ],

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"factoryID\": \"xxx\",\n\t\"username\": \"xxx\",\n\t\"phoneArea\": \"xxx\",\n\t\"isAdmin\": False\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"username\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/member.go",

        "groupTitle": "dental/member"
    },

    {

        "type": "get",

        "url": "/u/dental/oem/info/del/:tid/:tfid",

        "title": "齿科机构oem删除接口",

        "description": "<p>urlName: dentalFactoryOEMDelete</p>",

        "group": "dental/oem",

        "name": "dentalFactoryOEMDelete",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.admin_dental_member\", \"dental.audit_dental_list\", \"dental.manage_dental_member\"]"
            }
        ],

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "get",

        "url": "/u/dental/oem/info/gets/:tid",

        "title": "齿科机构oem列表接口",

        "description": "<p>urlName: dentalFactoryOEMList</p>",

        "group": "dental/oem",

        "name": "dentalFactoryOEMList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.admin_dental_member\", \"dental.audit_dental_list\", \"dental.manage_dental_member\"]"
            }
        ],

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n  \t\"result\": [{\n\t\t\"KeyName\": \"xxx\",\n\t\t\"KeyValue\": \"xxx\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "post",

        "url": "/u/dental/oem/info/set",

        "title": "齿科机构oem设置接口",

        "description": "<p>urlName: dentalFactoryOEMSetting</p>",

        "group": "dental/oem",

        "name": "dentalFactoryOEMSetting",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "permission": [

            {

                "name": "[\"dental.change_dental_list\",\"dental.audit_dental_list\", \"dental.manage_dental_member\"\"]"
            }
        ],

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"fid\": \"xxx\",\n\t\"position\": \"xxx\",\n\t\"cts\": [{\n\t\t\"id\": \"xxx\",\n\t\t\"deleted\": False,\n\t\t\"field\": \"xxx\",\n\t\t\"lang\": \"xxx\",\n\t\t\"content\": \"canceled\"\n\t}]\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"content\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "get",

        "url": "/oiga/:oemURL/:lang",

        "title": "齿科机构oem联系地址信息获取接口",

        "description": "<p>urlName: getOEMAreaInfo</p>",

        "group": "dental/oem",

        "name": "getOEMAreaInfo",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n\t\"result\": [{\n\t\t\"field\": \"亚太区\",\n\t\t\"content\": \"先临三维科技股份有限公司\\n电话: +86-571-82999050\\n地址: 浙江省杭州市萧山区闻堰街道湘滨路1398号\"\n\t}, {\n\t\t\"field\": \"客服邮箱\",\n\t\t\"content\": \"dental_support@shining3d.com\"\n\t}, {\n\t\t\"field\": \"欧洲区\",\n\t\t\"content\": \"SHINING 3D Technology GmbH.\\n电话: +49-711-28444089\\n地址: Panorama, Heilbronner straße 86, 70191, Stuttgart, Germany\"\n\t}, {\n\t\t\"field\": \"美洲区\",\n\t\t\"content\": \"SHINING 3D Technology Inc.\\n电话: +1-415-259-47879\\n地址: 1740 César Chávez St. Unit D. San Francisco, CA 94124, United States\"\n\t}],\n\t\"status\": \"success\"\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "get",

        "url": "/oig/:oemURL",

        "title": "齿科机构oem信息获取接口",

        "description": "<p>urlName: getOEMInfo</p>",

        "group": "dental/oem",

        "name": "getOEMInfo",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",
                    "content": "{\n \"result\": {\n  \"cn\": {\n   \"banner\": \"https://awscdn.dental3dcloud.com/home_banner.png\",\n   \"copyright\": \"先临三维科技股份有限公司\",\n   \"logo\": \"https://awscdn.dental3dcloud.com/logo.png\",\n   \"personalPolicy\": \"先临三维齿科云平台将个人信息用于以下目的，不会用于任何其他目的。\n\n. 确认客户加入先临三维齿科云平台的意向\n. 识别和认证服务的客户\n. 维持和管理会员资格\n. 提供服务\n. 发送相关信息\n. 保留期：直到成员选择离开\n. 收集数据：姓名、电子邮件地址、身份证、密码、电话号码、业务类型\",\n   \"promotionPolicy\": \"先临三维齿科云平台通过您注册的联系信息向您提供营销信息，以提供有关各种产品和促销的信息。\n我方根据相关法律法规获得营销使用许可。\n如果您同意将您的个人信息用于营销目的，您将获得有关新产品和服务更新的有用信息。\",\n   \"title\": \"先临三维齿科云平台\"\n  },\n  \"en\": {\n   \"banner\": \"https://awscdn.dental3dcloud.com/home_banner_en.png\",\n   \"copyright\": \"SHINING 3D TECH CO., LTD.\",\n   \"logo\": \"https://awscdn.dental3dcloud.com/logo.png\",\n   \"personalPolicy\": \"Shining3D dental cloud will use personal information for the following purposes and will not use it for any other purpose.\n. To confirm customers’ intention to join Shining3D dental cloud\n. To identify and certify customers for the service\n. To maintain and manage membership\n. To supply services and\n. To send relevant information.\n. Retention period : until a member chooses to leave\n. Collecting data : Name, E-mail address, ID, Password, phone number, type of business\",\n   \"promotionPolicy\": \"Shining3D dental cloud provides marketing information to you via your registered contact information for the purpose of providing information about various products and promotions. \nWe obtain marketing use consent in accordance with relevant laws and regulations. \nIf you agree to allow use of your personal information for marketing purposes, you will be provided with useful information about new products and service updates accordingly.\",\n   \"title\": \"Shining3D Dental Cloud\"\n  },\n  \"ja\": {\n   \"banner\": \"https://awscdn.dental3dcloud.com/home_banner_en.png\",\n   \"copyright\": \"SHINING 3D TECH CO., LTD.\",\n   \"logo\": \"https://awscdn.dental3dcloud.com/logo.png\",\n   \"personalPolicy\": \"Shining3D dental cloud will use personal information for the following purposes and will not use it for any other purpose.\n. To confirm customers’ intention to join Shining3D dental cloud\n. To identify and certify customers for the service\n. To maintain and manage membership\n. To supply services and\n. To send relevant information.\n. Retention period : until a member chooses to leave\n. Collecting data : Name, E-mail address, ID, Password, phone number, type of business\",\n   \"promotionPolicy\": \"Shining3D dental cloud provides marketing information to you via your registered contact information for the purpose of providing information about various products and promotions. \nWe obtain marketing use consent in accordance with relevant laws and regulations. \nIf you agree to allow use of your personal information for marketing purposes, you will be provided with useful information about new products and service updates accordingly.\",\n   \"title\": \"Shining3D Dental Cloud\"\n  }\n },\n \"status\": \"success\"\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "get",

        "url": "/oigpc/:oemURL/:lang/:privacyType",

        "title": "齿科机构oem各类政策/颜色信息获取接口",

        "description": "<p>urlName: getOEMPrivacyColorInfoByType</p>",

        "group": "dental/oem",

        "name": "getOEMPrivacyColorInfoByType",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n\t\"result\": \"xxx\",\n\t\"status\": \"success\"\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/institution.go",

        "groupTitle": "dental/oem"
    },

    {

        "type": "get",

        "url": "/u/dental/list",

        "title": "齿科订单列表接口",

        "description": "<p>urlName: dentalList</p>",

        "deprecated": True,

        "group": "dental/order",

        "name": "dentalList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "startOn",

                        "description": "<p>Optional 下单时间的最早时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "endOn",

                        "description": "<p>Optional 下单时间的最晚时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "patientName",

                        "description": "<p>Optional 患者姓名，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "labName",

                        "description": "<p>Optional 技工所名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "doctorName",

                        "description": "<p>Optional 医生名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "status",

                        "description": "<p>Optional 状态，只有 waitAccept/waitDesign/waitDelivery/waitConfirmDesign/canceled/finished/waitConfirmDelivery/closed/refused</p>"
                    }
                ]
            }
        },

        "success": {

            "fields": {

                "Success 200": [

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "page",

                        "description": "<p>当前页号</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pageSize",

                        "description": "<p>每页条数，默认是50</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pages",

                        "description": "<p>总页数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "total",

                        "description": "<p>总记录数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Attachs",

                        "description": "<p>是附件对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "CreateBy",

                        "description": "<p>是创建人对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "ChangeBy",

                        "description": "<p>是更新人对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Lab",

                        "description": "<p>是技工所对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Doctor",

                        "description": "<p>是医生对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Comments",

                        "description": "<p>Optional 订单的消息列表字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "IssueAdmins",

                        "description": "<p>是下单方的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "LabAdmins",

                        "description": "<p>是技工所的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "LabMembers",

                        "description": "<p>是技工所成员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "ChangeOn/CreateOn",

                        "description": "<p>是UTC时间，CreateOn是下单时间</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "DesignDfsID",

                        "description": "<p>确定的设计方案上传附件id，注意如果是多个同1方案的附件，会以逗号进行分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "DeliverySupplior",

                        "description": "<p>物流供应商</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "DeliveryNum",

                        "description": "<p>物流单号</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n    \"page\": 1,\n    \"pageSize\": 50,\n    \"pages\": 1,\n    \"total\": 6\n  },\n  \"result\": [{\n\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\"ChangeBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\"Client\": \"{\\\"modelCode\\\":\\\"dental\\\",\\\"serialNum\\\":\\\"xxx\\\",\\\"softName\\\":\\\"detnal\\\",\\\"softVer\\\":\\\"3.0.0.0\\\",\\\"uniqueInstallCode\\\":\\\"dsfads\\\",\\\"uniqueUsageCode\\\":\\\"fads2\\\"}\",\n\t\"Content\": \"{}\",\n\t\"CreateBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\"Doctor\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\"IssueAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"LabAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"LabMembers\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"IsDeleted\": \"\",\n\t\"Lab\": \"{\\\"Name\\\":\\\"Shining3d\\\",\\\"ID\\\":\\\"1\\\"}\",\n\t\"Lang\": \"cn\",\n\t\"DesignDfsID\":\"\",\n\t\"DeliveryNum\":\"\",\n\t\"DeliverySupplior\":\"\",\n\t\"DesignType\": \"repair\",\n\t\"Materials\": \"xxx,xxx\",\n\t\"Tooths\": \"11,12\",\n\t\"DesignOptions\": \"crown,surgicalguide\",\n\t\"DentalNotation\": \"FDI\",\n\t\"NeedConfirm\": True,\n\t\"IsBeb\": False,\n\t\"Notes\": \"notes\",\n\t\"PatientName\": \"patient_name\",\n\t\"Comments\": '[{\"ID\":\"13960841-ee4e-566f-837d-c5a6e89e68f0\",\"CreateOn\":\"2019-01-24 07:53:15\",\"ChangeOn\":\"2019-01-24 07:53:15\",\"Content\":\"dsd\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[]},{\"ID\":\"2ab22be9-4260-5450-86b4-96cd5b693787\",\"CreateOn\":\"2019-01-24 09:47:35\",\"ChangeOn\":\"2019-01-24 09:47:35\",\"Content\":\"\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[{\"FileName\":\"3dhda20190111.csv\",\"CreateBy\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"CreateOn\":\"2019-01-24 17:47:31\",\"DfsID\":\"dentalComment/948f4f88220a1711b70f4f8b67a4551a\"},{\"FileName\":\"3ddlf20190111.csv\",\"CreateBy\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"CreateOn\":\"2019-01-24 17:47:22\",\"DfsID\":\"dentalComment/45cd95a1b8a681865875d676da64b4a4\"}]},{\"ID\":\"f347bac6-073a-5d14-bc9c-1b404702e4f7\",\"CreateOn\":\"2019-01-24 07:46:55\",\"ChangeOn\":\"2019-01-24 07:46:55\",\"Content\":\"\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[{\"FileName\":\"QQ20180205-090318.png\",\"CreateBy\":\"560b5a52c23aaf15392f4bc1\",\"CreateOn\":\"2019-01-03 18:28:06\",\"DfsID\":\"dentalComment/ede0cad087840f131b5d87a2ca150e17\"}]}]',\n\t\"Status\": \"canceled\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/action/:tid/:taction",

        "title": "订单确认接单/确认收货/确认设计方案/关闭订单/拒绝接单/取消订单/要求重新发货接口",

        "description": "<p>urlName: dentalOrderAction</p>",

        "group": "dental/order",

        "name": "dentalOrderAction",

        "deprecated": True,

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "tid",

                        "description": "<p>是订单id mock状态下如果传xxx则会返回失败，其它值为成功</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "taction",

                        "description": "<p>是目标操作值，分为confirmReceive/refuseReceive/cancel/confirmDesign/confirmDelivery/redelivery/close</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/o/action",

        "title": "订单行为接口",

        "description": "<p>urlName: dentalOrderActions</p>",

        "group": "dental/order",

        "name": "dentalOrderActions",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "action",

                        "description": "<p>行为</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[String]",

                        "optional": False,

                        "field": "id",

                        "description": "<p>订单id</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": [\"xxxx\"],\n\t \"action\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"id\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/detail/:tid",

        "title": "订单单个查询接口",

        "description": "<p>urlName: dentalOrderDetail</p>",

        "deprecated": True,

        "group": "dental/order",

        "name": "dentalOrderDetail",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "tid",

                        "description": "<p>订单id</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\t\"ChangeBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\t\"Client\": \"{\\\"modelCode\\\":\\\"dental\\\",\\\"serialNum\\\":\\\"xxx\\\",\\\"softName\\\":\\\"detnal\\\",\\\"softVer\\\":\\\"3.0.0.0\\\",\\\"uniqueInstallCode\\\":\\\"dsfads\\\",\\\"uniqueUsageCode\\\":\\\"fads2\\\"}\",\n\t\t\"Content\": \"{}\",\n\t\t\"CreateBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\t\"Doctor\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\t\"IssueAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"LabAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"LabMembers\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"IsDeleted\": \"\",\n\t\t\"IsBeb\": False,\n\t\t\"Lab\": \"{\\\"Name\\\":\\\"Shining3d\\\",\\\"ID\\\":\\\"1\\\"}\",\n\t\t\"Lang\": \"cn\",\n\t\t\"DesignDfsID\":\"\",\n\t\t\"DeliveryNum\":\"\",\n\t\t\"DeliverySupplior\":\"\",\n\t\t\"DesignType\": \"repair\",\n\t\t\"Materials\": \"xxx,xxx\",\n\t\t\"Tooths\": \"11,12\",\n\t\t\"DesignOptions\": \"crown,surgicalguide\",\n\t\t\"DentalNotation\": \"FDI\",\n\t\t\"NeedConfirm\": True,\n\t\t\"Notes\": \"notes\",\n\t\t\"PatientName\": \"patient_name\",\n\t\t\"Comments\": '[{\"ID\":\"13960841-ee4e-566f-837d-c5a6e89e68f0\",\"CreateOn\":\"2019-01-24 07:53:15\",\"ChangeOn\":\"2019-01-24 07:53:15\",\"Content\":\"dsd\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[]},{\"ID\":\"2ab22be9-4260-5450-86b4-96cd5b693787\",\"CreateOn\":\"2019-01-24 09:47:35\",\"ChangeOn\":\"2019-01-24 09:47:35\",\"Content\":\"\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[{\"FileName\":\"3dhda20190111.csv\",\"CreateBy\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"CreateOn\":\"2019-01-24 17:47:31\",\"DfsID\":\"dentalComment/948f4f88220a1711b70f4f8b67a4551a\"},{\"FileName\":\"3ddlf20190111.csv\",\"CreateBy\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"CreateOn\":\"2019-01-24 17:47:22\",\"DfsID\":\"dentalComment/45cd95a1b8a681865875d676da64b4a4\"}]},{\"ID\":\"f347bac6-073a-5d14-bc9c-1b404702e4f7\",\"CreateOn\":\"2019-01-24 07:46:55\",\"ChangeOn\":\"2019-01-24 07:46:55\",\"Content\":\"\",\"TargetID\":\"3fccbb42822f8d1d296ee651889fd399\",\"ChangeBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"CreateBy\":{\"NickName\":\"孙博\",\"UserID\":\"a0c6c5d0-c760-4a33-b7fb-10eb90c0ed34\",\"Email\":\"sunbo@shining3d.com\",\"Phone\":\"\",\"PhoneArea\":\"\"},\"Attachs\":[{\"FileName\":\"QQ20180205-090318.png\",\"CreateBy\":\"560b5a52c23aaf15392f4bc1\",\"CreateOn\":\"2019-01-03 18:28:06\",\"DfsID\":\"dentalComment/ede0cad087840f131b5d87a2ca150e17\"}]}]',\n\t\t\"Status\": \"canceled\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/edit",

        "title": "订单更新接口",

        "description": "<p>urlName: dentalOrderEdit 注意只有待接单waitAccept或是被拒绝refused状态的订单才能更新，同时操作人是下单的医生或是机构管理员，更新后需要技工所重新走接单确认流程</p>",

        "group": "dental/order",

        "name": "dentalOrderEdit",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "lang",

                        "description": "<p>语言，默认是cn，英文是en，是2位字母的语言缩写，具体可见网页：https://www.science.co.il/language/Locale-codes.php</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "notes",

                        "description": "<p>Optional 订单其他要求</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "doctorId",

                        "description": "<p>医生用户id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "id",

                        "description": "<p>订单id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "bool",

                        "optional": True,

                        "field": "needConfirm",

                        "description": "<p>是否需要确认，默认是True</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "bool",

                        "optional": True,

                        "field": "isBeb",

                        "description": "<p>是否私有格式，默认是False</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "labId",

                        "description": "<p>技工所id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "designType",

                        "description": "<p>设计类型，是修复还是正畸,修复是repair，正畸是orthodontic</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]Integer",

                        "optional": True,

                        "field": "tooths",

                        "description": "<p>牙位，当设计类型是repair时必须提供，注意是整数型数组</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "dentalNotation",

                        "description": "<p>牙位标记法，当设计类型是repair时必须提供</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]String",

                        "optional": True,

                        "field": "materials",

                        "description": "<p>材料，当设计类型是repair时必须提供，注意是字符型数组</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]String",

                        "optional": True,

                        "field": "designOptions",

                        "description": "<p>设计内容，当设计类型是repair时必须提供，注意是字符型数组，比如牙冠等</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "modelCode",

                        "description": "<p>Optional 设备型号唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "serialNum",

                        "description": "<p>Optional 设备序列号</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softName",

                        "description": "<p>软件名称唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softVer",

                        "description": "<p>软件版本，必须是1.0.0.0类似的格式，只允许.和数字</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueInstallCode",

                        "description": "<p>软件在客户端安装后的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueUsageCode",

                        "description": "<p>软件在客户端启动时的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "content",

                        "description": "<p>是case信息的完整json格式序列化后的字符串，注意后续有可能是要对此内容解开分析的，所以软件端要注意前后的兼容性</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "attachType",

                        "description": "<p>是附件类型,值有designData/full/other/preview/scanData</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "dfsID",

                        "description": "<p>是附件上传后得到的返回值中dfs_id</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": \"xxxx\",\n\t \"lang\": \"cn\",\n\t \"notes\": \"\",\n\t \"doctorId\": \"xxx\",\n\t \"labId\": \"xxx\",\n\t \"designType\":\"repair\",\n\t \"tooths\":[1,2],\n\t \"materials\":[\"xxx\",\"xxx\"],\n\t \"designOptions\":[\"xxx\",\"xxx\"],\n\t \"dentalNotation\":\"FDI\",\n\t \"needConfirm\": True,\n\t \"isBeb\": True,\n\t \"client\": {\n\t\t \"modelCode\": \"xxx\",\n\t\t \"serialNum\": \"xxx\",\n\t\t \"softName\": \"xxx\",\n\t\t \"softVer\": \"1.0.0.0\",\n\t\t \"uniqueInstallCode\": \"xxx\",\n\t\t \"uniqueUsageCode\": \"xxx\"\n\t },\n\t \"attachs\": [{\n\t\t \"attachType\":\"xxx\",\n\t\t \"dfsID\":\"xxx\"\n\t }],\n\t \"content\":\"xxx\",\n\t \"patientName\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\"ChangeBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\"Client\": \"{\\\"modelCode\\\":\\\"dental\\\",\\\"serialNum\\\":\\\"xxx\\\",\\\"softName\\\":\\\"detnal\\\",\\\"softVer\\\":\\\"3.0.0.0\\\",\\\"uniqueInstallCode\\\":\\\"dsfads\\\",\\\"uniqueUsageCode\\\":\\\"fads2\\\"}\",\n\t\"Content\": \"{}\",\n\t\"CreateBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\"Doctor\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\"IssueAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"LabAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"LabMembers\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\"IsDeleted\": \"\",\n\t\"IsBeb\": False,\n\t\"Lab\": \"{\\\"Name\\\":\\\"Shining3d\\\",\\\"ID\\\":\\\"1\\\"}\",\n\t\"Lang\": \"cn\",\n\t\"DesignDfsID\":\"\",\n\t\"DeliveryNum\":\"\",\n\t\"DeliverySupplior\":\"\",\n\t\"DesignType\": \"repair\",\n\t\"Materials\": \"xxx,xxx\",\n\t\"Tooths\": \"11,12\",\n\t\"DesignOptions\": \"crown,surgicalguide\",\n\t\"DentalNotation\": \"FDI\",\n\t\"NeedConfirm\": True,\n\t\"Notes\": \"notes\",\n\t\"PatientName\": \"patient_name\",\n\t\"Status\": \"canceled\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/add",

        "title": "订单发布接口",

        "description": "<p>urlName: dentalOrderIssue</p>",

        "group": "dental/order",

        "name": "dentalOrderIssue",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "lang",

                        "description": "<p>语言，默认是cn，英文是en，是2位字母的语言缩写，具体可见网页：https://www.science.co.il/language/Locale-codes.php</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "notes",

                        "description": "<p>Optional 订单其他要求</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "doctorId",

                        "description": "<p>医生用户id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "bool",

                        "optional": True,

                        "field": "needConfirm",

                        "description": "<p>是否需要确认，默认是True</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "bool",

                        "optional": True,

                        "field": "isBeb",

                        "description": "<p>是否私有格式，默认是False</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "labId",

                        "description": "<p>技工所id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "designType",

                        "description": "<p>设计类型，是修复还是正畸,修复是repair，正畸是orthodontic</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]Integer",

                        "optional": True,

                        "field": "tooths",

                        "description": "<p>牙位，当设计类型是repair时必须提供，注意是整数型数组</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]String",

                        "optional": True,

                        "field": "materials",

                        "description": "<p>材料，当设计类型是repair时必须提供，注意是字符型数组</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "dentalNotation",

                        "description": "<p>牙位标记法，当设计类型是repair时必须提供</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[]String",

                        "optional": True,

                        "field": "designOptions",

                        "description": "<p>设计内容，当设计类型是repair时必须提供，注意是字符型数组，比如牙冠等</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "modelCode",

                        "description": "<p>Optional 设备型号唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "patientName",

                        "description": "<p>Optional 患者姓名</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "serialNum",

                        "description": "<p>Optional 设备序列号</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softName",

                        "description": "<p>软件名称唯一名，是型号中维护进去的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "softVer",

                        "description": "<p>软件版本，必须是1.0.0.0类似的格式，只允许.和数字</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueInstallCode",

                        "description": "<p>软件在客户端安装后的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "uniqueUsageCode",

                        "description": "<p>软件在客户端启动时的唯一id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "content",

                        "description": "<p>是case信息的完整json格式序列化后的字符串，注意后续有可能是要对此内容解开分析的，所以软件端要注意前后的兼容性</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "attachType",

                        "description": "<p>是附件类型,值有designData/full/other/preview/scanData</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "dfsID",

                        "description": "<p>是附件上传后得到的返回值中dfs_id</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"lang\": \"cn\",\n\t \"notes\": \"\",\n\t \"doctorId\": \"xxx\",\n\t \"labId\": \"xxx\",\n\t \"designType\":\"repair\",\n\t \"tooths\":[1,2],\n\t \"materials\":[\"xxx\",\"xxx\"],\n\t \"designOptions\":[\"xxx\",\"xxx\"],\n\t \"dentalNotation\":\"FDI\",\n\t \"needConfirm\": True,\n\t \"isBeb\": False,\n\t \"client\": {\n\t\t \"modelCode\": \"xxx\",\n\t\t \"serialNum\": \"xxx\",\n\t\t \"softName\": \"xxx\",\n\t\t \"softVer\": \"1.0.0.0\",\n\t\t \"uniqueInstallCode\": \"xxx\",\n\t\t \"uniqueUsageCode\": \"xxx\"\n\t },\n\t \"attachs\": [{\n\t\t \"attachType\":\"xxx\",\n\t\t \"dfsID\":\"xxx\"\n\t }],\n\t \"content\":\"xxx\",\n\t \"patientName\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\t\"ChangeBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\t\"Client\": \"{\\\"modelCode\\\":\\\"dental\\\",\\\"serialNum\\\":\\\"xxx\\\",\\\"softName\\\":\\\"detnal\\\",\\\"softVer\\\":\\\"3.0.0.0\\\",\\\"uniqueInstallCode\\\":\\\"dsfads\\\",\\\"uniqueUsageCode\\\":\\\"fads2\\\"}\",\n\t\t\"Content\": \"{}\",\n\t\t\"CreateBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\t\"Doctor\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\t\"IssueAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"LabAdmins\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"LabMembers\": { String: '59d7fe8848da0edc0b2ffd3cb6,59d7feda0edc0b2ffd3cb6', Valid: True },\n\t\t\"IsDeleted\": \"\",\n\t\t\"IsBeb\": False,\n\t\t\"Lab\": \"{\\\"Name\\\":\\\"Shining3d\\\",\\\"ID\\\":\\\"1\\\"}\",\n\t\t\"Lang\": \"cn\",\n\t\t\"DesignDfsID\":\"\",\n\t\t\"DeliveryNum\":\"\",\n\t\t\"DeliverySupplior\":\"\",\n\t\t\"DesignType\": \"repair\",\n\t\t\"Materials\": \"xxx,xxx\",\n\t\t\"Tooths\": \"11,12\",\n\t\t\"DesignOptions\": \"crown,surgicalguide\",\n\t\t\"DentalNotation\": \"FDI\",\n\t\t\"NeedConfirm\": True,\n\t\t\"Notes\": \"notes\",\n\t\t\"PatientName\": \"patient_name\",\n\t\t\"Status\": \"canceled\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/oc/list",

        "title": "齿科订单列表客户端接口",

        "description": "<p>urlName: dentalOrderList</p>",

        "deprecated": True,

        "group": "dental/order",

        "name": "dentalOrderList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "startOn",

                        "description": "<p>Optional 下单时间的最早时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "endOn",

                        "description": "<p>Optional 下单时间的最晚时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "patientName",

                        "description": "<p>Optional 患者姓名，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "labName",

                        "description": "<p>Optional 技工所名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "doctorName",

                        "description": "<p>Optional 医生名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "status",

                        "description": "<p>Optional 状态，只有 waitAccept/waitDesign/waitDelivery/waitConfirmDesign/canceled/finished/waitConfirmDelivery/closed/refused</p>"
                    }
                ]
            }
        },

        "success": {

            "fields": {

                "Success 200": [

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "page",

                        "description": "<p>当前页号</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pageSize",

                        "description": "<p>每页条数，默认是50</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pages",

                        "description": "<p>总页数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "total",

                        "description": "<p>总记录数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Attachs",

                        "description": "<p>是附件对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Lab",

                        "description": "<p>是技工所对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "Doctor",

                        "description": "<p>是医生对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "IssueAdmins",

                        "description": "<p>是下单方的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "LabAdmins",

                        "description": "<p>是技工所的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Object",

                        "optional": False,

                        "field": "LabMembers",

                        "description": "<p>是技工所成员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "ChangeOn/CreateOn",

                        "description": "<p>是UTC时间，CreateOn是下单时间</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "DeliverySupplior",

                        "description": "<p>物流供应商</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "DeliveryNum",

                        "description": "<p>物流单号</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n    \"page\": 1,\n    \"pageSize\": 50,\n    \"pages\": 1,\n    \"total\": 6\n  },\n  \"result\": [{\n\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\"Content\": \"xxx\",\n\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\"Doctor\": \"xxx\",\n\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\"IssueAdmins\": \"xxx\",\n\t\"LabAdmins\": \"xxx\",\n\t\"LabMembers\": \"xxx\",\n\t\"Lab\": \"xxx\",\n\t\"Hospitals\": \"xxx\",\n\t\"DoctorID\":\"\",\n\t\"HospitalID\":\"\",\n\t\"DeliveryNum\":\"\",\n\t\"DeliverySupplior\":\"\",\n\t\"DesignType\": \"repair\",\n\t\"PatientName\": \"patient_name\",\n\t\"Status\": \"canceled\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/logistics",

        "title": "订单发货接口",

        "description": "<p>urlName: dentalOrderLogistics 注意只有waitDelivery/waitConfirmDelivery状态的订单，同时操作人是技工所成员</p>",

        "group": "dental/order",

        "name": "dentalOrderLogistics",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "id",

                        "description": "<p>是订单id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "supplior",

                        "description": "<p>是物流提供方</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "num",

                        "description": "<p>是物流单号</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": \"xxxx\",\n\t \"supplior\": \"xxx\",\n\t \"num\": \"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/redesign",

        "title": "订单要求重新设计接口",

        "description": "<p>urlName: dentalOrderRedesign 注意只有waitConfirmDesign状态的订单，同时操作人是下单的医生或是机构管理员，提交后将变更订单状态，同时提交的内容作为1个新的评论</p>",

        "group": "dental/order",

        "name": "dentalOrderRedesign",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "id",

                        "description": "<p>订单id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "notes",

                        "description": "<p>Optional 重新设计要求的内容, notes和dfsIDs必须至少存在1个</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[String]",

                        "optional": True,

                        "field": "dfsIDs",

                        "description": "<p>附件dfsID数组, notes和dfsIDs必须至少存在1个</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": \"xxxx\",\n\t \"notes\": \"\",\n\t \"dfsIDs\": [\"xxx\"]\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "post",

        "url": "/u/dental/uploaddesign",

        "title": "订单上传设计接口",

        "description": "<p>urlName: dentalOrderUploadDesign</p>",

        "group": "dental/order",

        "name": "dentalOrderUploadDesign",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": False,

                        "field": "id",

                        "description": "<p>订单id</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "notes",

                        "description": "<p>Optional 设计的说明</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "[String]",

                        "optional": False,

                        "field": "dfsIDs",

                        "description": "<p>设计附件dfsID数组</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": \"xxxx\",\n\t \"notes\": \"\",\n\t \"dfsIDs\": [\"xxx\"]\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"password\\\":\\\"password not match.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/o/list",

        "title": "齿科订单列表云平台接口",

        "description": "<p>urlName: dentalorderCloudList</p>",

        "deprecated": True,

        "group": "dental/order",

        "name": "dentalorderCloudList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "startOn",

                        "description": "<p>Optional 下单时间的最早时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "endOn",

                        "description": "<p>Optional 下单时间的最晚时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "patientName",

                        "description": "<p>Optional 患者姓名，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "labName",

                        "description": "<p>Optional 技工所名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "doctorName",

                        "description": "<p>Optional 医生名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "status",

                        "description": "<p>Optional 状态，只有 waitAccept/waitDesign/waitDelivery/waitConfirmDesign/canceled/finished/waitConfirmDelivery/closed/refused</p>"
                    }
                ]
            }
        },

        "success": {

            "fields": {

                "Success 200": [

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "page",

                        "description": "<p>当前页号</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pageSize",

                        "description": "<p>每页条数，默认是50</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pages",

                        "description": "<p>总页数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "total",

                        "description": "<p>总记录数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "lab",

                        "description": "<p>是技工所对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "doctor",

                        "description": "<p>是医生对象的json序列化字符串</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "issueAdmins",

                        "description": "<p>是下单方的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "labAdmins",

                        "description": "<p>是技工所的机构管理员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "labMembers",

                        "description": "<p>是技工所成员user_id数组字符串，逗号分隔</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "createOn",

                        "description": "<p>是UTC时间，CreateOn是下单时间</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "deliverySupplior",

                        "description": "<p>物流供应商</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "String",

                        "optional": False,

                        "field": "deliveryNum",

                        "description": "<p>物流单号</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n    \"page\": 1,\n    \"pageSize\": 50,\n    \"pages\": 1,\n    \"total\": 6\n  },\n  \"result\": [{\n\t\"lab\": \"xxx\",\n\t\"content\": \"xxx\",\n\t\"createOn\": \"2018-12-24T07:10:04Z\",\n\t\"doctor\": \"xxx\",\n\t\"id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\"issueAdmins\": \"xxx\",\n\t\"labAdmins\": \"xxx\",\n\t\"labMembers\": \"xxx\",\n\t\"deliveryNum\":\"\",\n\t\"hospitals\":\"\",\n\t\"hospitalID\":\"\",\n\t\"doctorID\":\"\",\n\t\"deliverySupplior\":\"\",\n\t\"designType\": \"repair\",\n\t\"patientName\": \"patient_name\",\n\t\"status\": \"canceled\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/comment/:tid",

        "title": "齿科订单列表接口",

        "description": "<p>urlName: orderCommentList</p>",

        "group": "dental/order",

        "name": "orderCommentList",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "page",

                        "description": "<p>Optional 请求第几页</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "Integer",

                        "optional": True,

                        "field": "pageSize",

                        "description": "<p>Optional 请求每页条数</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "startOn",

                        "description": "<p>Optional 下单时间的最早时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "endOn",

                        "description": "<p>Optional 下单时间的最晚时间，要求2018-12-24T07:10:04Z这样的格式，当作utc时间</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "patientName",

                        "description": "<p>Optional 患者姓名，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "labName",

                        "description": "<p>Optional 技工所名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "doctorName",

                        "description": "<p>Optional 医生名称，支持模糊查询</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "status",

                        "description": "<p>Optional 状态，只有 waitAccept/waitDesign/waitDelivery/waitConfirmDesign/canceled/finished/waitConfirmDelivery/closed/refused</p>"
                    }
                ]
            }
        },

        "success": {

            "fields": {

                "Success 200": [

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "page",

                        "description": "<p>当前页号</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pageSize",

                        "description": "<p>每页条数，默认是50</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "pages",

                        "description": "<p>总页数</p>"
                    },

                    {

                        "group": "Success 200",

                        "type": "Integer",

                        "optional": False,

                        "field": "total",

                        "description": "<p>总记录数</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n    \"pageInfo\": {\n    \"page\": 1,\n    \"pageSize\": 50,\n    \"pages\": 1,\n    \"total\": 6\n  },\n  \"result\": [{\n\t\"Attachs\": \"[{\\\"AttachType\\\":\\\"designData\\\",\\\"DfsID\\\":\\\"quill/10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"CreateOn\\\":\\\"2018-12-24T07:10:04Z\\\",\\\"CreateBy\\\":\\\"10a893b2aaba6a6c0d600fb8548bb49a\\\",\\\"FileName\\\":\\\"quill.jpg\\\",\\\"Ext\\\":\\\"jpg\\\",\\\"SrcDfsID\\\":\\\"xxx\\\",\\\"ID\\\":\\\"xxx\\\",\\\"Status\\\":\\\"init\\\",\\\"Bucket\\\":\\\"init\\\",\\\"Endpoint\\\":\\\"init\\\",\\\"Notes\\\":\\\"init\\\",\\\"Version\\\":\\\"init\\\",\\\"Err\\\":\\\"init\\\"}]\",\n\t\"ChangeBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"ChangeOn\": \"2018-12-24T07:10:04Z\",\n\t\"Content\": \"{}\",\n\t\"CreateBy\": \"{\\\"NickName\\\":\\\"victor.wu\\\",\\\"UserID\\\":\\\"560b5a52c23aaf15392f4bc1\\\",\\\"Email\\\":\\\"victor@shining3d.com\\\",\\\"Phone\\\":\\\"18969979799\\\",\\\"PhoneArea\\\":\\\"86\\\"}\",\n\t\"CreateOn\": \"2018-12-24T07:10:04Z\",\n\t\"Id\": \"59d7fe8848da0edc0b2ffd3cb69d6912\",\n\t\"TargetID\": \"\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/comment.go",

        "groupTitle": "dental/order"
    },

    {

        "type": "get",

        "url": "/u/dental/o/top",

        "title": "齿科订单趋势统计接口",

        "description": "<p>urlName: dentalOrderTop</p>",

        "deprecated": True,

        "group": "dental/statistics",

        "name": "dentalOrderTop",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n\t\"status\":\"success\",\n\t\"result\": [{\n\t\t\"totals\": \"xxx\",\n\t\t\"class\": \"xxx\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/statistics"
    },

    {

        "type": "get",

        "url": "/u/dental/o/totals",

        "title": "齿科订单总数统计接口",

        "description": "<p>urlName: dentalOrderTotals</p>",

        "deprecated": True,

        "group": "dental/statistics",

        "name": "dentalOrderTotals",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n\t\"status\":\"success\",\n\t\"result\": {\n\t\t\"totals\": \"xxx\",\n\t\t\"waitReceive\": \"xxx\",\n\t\t\"hasLogistics\": \"xxx\",\n\t\t\"hasIM\": \"xxx\",\n\t\t\"hasDesign\": \"xxx\"\n    }\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/statistics"
    },

    {

        "type": "get",

        "url": "/u/dental/o/trend",

        "title": "齿科订单趋势统计接口",

        "description": "<p>urlName: dentalOrderTrend</p>",

        "deprecated": True,

        "group": "dental/statistics",

        "name": "dentalOrderTrend",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": " {\n\t\"status\":\"success\",\n\t\"result\": [{\n\t\t\"totals\": \"xxx\",\n\t\t\"class\": \"xxx\"\n    }]\n }",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/order.go",

        "groupTitle": "dental/statistics"
    },

    {

        "type": "post",

        "url": "/u/dental/comment/add",

        "title": "订单消息新加接口",

        "description": "<p>urlName: orderCommentAdd</p>",

        "group": "dental",

        "name": "orderCommentAdd",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    },

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-Token",

                        "description": "<p>Required 您的应用用户登录时获取到的token</p>"
                    }
                ]
            }
        },

        "parameter": {

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t \"id\": \"xxx\",\n\t \"notes\": \"xxx\",\n\t \"dfsIDs\": [\"xxx\"]\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"notes\\\":\\\"password not be empty.\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/comment.go",

        "groupTitle": "dental"
    },

    {

        "type": "post",

        "url": "/da/reg",

        "title": "齿科云平台注册接口",

        "description": "<p>urlName: regDental</p>",

        "group": "dental",

        "name": "regDental",

        "header": {

            "fields": {

                "Header": [

                    {

                        "group": "Header",

                        "type": "String",

                        "optional": False,

                        "field": "X-Auth-AppId",

                        "description": "<p>Required 您的应用获取到的appid</p>"
                    }
                ]
            }
        },

        "parameter": {

            "fields": {

                "Parameter": [

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "name",

                        "description": "<p>机构名称，为机构时必须</p>"
                    },

                    {

                        "group": "Parameter",

                        "type": "String",

                        "optional": True,

                        "field": "oemDomain",

                        "description": "<p>来源，默认为index</p>"
                    }
                ]
            },

            "examples": [

                {

                    "title": "Request-Example:",

                    "content": "{\n\t\"name\": \"xxxx\",\n\t\"instituationType\": \"xxxx\",\n\t\"uuid\":\"xxx\",\n\t\"captcha\":\"xxx\",\n\t\"validCode\":\"xxx\",\n\t\"nickName\":\"xxx\",\n\t\"username\":\"xxx\",\n\t\"phoneArea\":\"xxx\",\n\t\"enablePromotion\":\"xxx\",\n\t\"oemDomain\":\"xxx\",\n\t\"password\":\"xxx\"\n}",

                    "type": "json"
                }
            ]
        },

        "success": {

            "examples": [

                {

                    "title": "Success-Response",

                    "content": "{\n    \"status\": \"success\",\n    \"result\": \"\"\n}",

                    "type": "json"
                }
            ]
        },

        "error": {

            "examples": [

                {

                    "title": "Error-Response:",

                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"username\\\":\\\"serverErr\\\"}\"\n    }\n}",

                    "type": "json"
                }
            ]
        },

        "version": "0.0.0",

        "filename": "services/account.go",

        "groupTitle": "dental"
    }
]

from jsonpath import jsonpath
from json import dumps
import ast


def get_all_case(_apiInfo):
    title = _apiInfo.get("title", "")
    group = _apiInfo.get("group", "")
    url = _apiInfo.get("url", "")
    method = _apiInfo.get("type", "")
    data = jsonpath(_apiInfo, "$..parameter.examples..content")
    data = ast.literal_eval(data[0].replace(",,", ",")) if data else ""
    return ("采集微服务", group, title, url, method, "", "", dumps(data), "json", 200, "success")


if __name__ == '__main__':
    for i in get_all_case(apiInfo[0]):
        print(i)
