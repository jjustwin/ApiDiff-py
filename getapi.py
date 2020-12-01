false = False
true = True
apiInfo = [
    {
        "type": "post",
        "url": "/activeDD",
        "title": "齿科设备激活接口",
        "description": "<p>urlName: activeDD</p>",
        "group": "dental/device",
        "name": "activeDD",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": false,
                        "field": "modelCode",
                        "description": "<p>设备型号唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "serialNum",
                        "description": "<p>设备序列号且必须是入库记录中有的</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softModelCode",
                        "description": "<p>软件型号唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "ver",
                        "description": "<p>软件版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t \"modelCode\": \"xxx\",\n\t \"serialNum\": \"xxx\",\n\t \"softModelCode\": \"xxx\",\n\t \"ver\": \"xxx\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": "{\n    \"status\": \"success\",\n    \"result\":  \"\"\n}",
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
        "filename": "services/tracing.go",
        "groupTitle": "dental/device"
    },
    {
        "type": "post",
        "url": "/dtta?type=form",
        "title": "定制表单结果提交",
        "description": "<p>urlName: tracing  推送的定制表单，在用户提交后得到的结果</p>",
        "group": "push",
        "name": "formTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "content",
                        "description": "<p>内容，一般是json的对象字符串</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"form\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":\"{}\"\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "push"
    },
    {
        "type": "post",
        "url": "/dtta?type=aliReport",
        "title": "aliReport记录",
        "description": "<p>urlName: tracing  用户端软件或硬件aliReport记录</p>",
        "group": "tracing",
        "name": "aliReportTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "content",
                        "description": "<p>内容，一般是数据文件上传后的内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "source",
                        "description": "<p>来源</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"aliReport\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\": \"xxx\"\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=aliUpgrade",
        "title": "阿里鞋测量升级记录跟踪",
        "description": "<p>urlName: aliUpgrade  阿里鞋测量升级记录跟踪</p>",
        "group": "tracing",
        "name": "aliUpgradeTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "deviceId",
                        "description": "<p>硬盘id</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "algorighmVer",
                        "description": "<p>算法版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sdkVer",
                        "description": "<p>软件sdk版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "communityVer",
                        "description": "<p>通讯sdk版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "firmwareVer",
                        "description": "<p>硬件固件版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "frontVer",
                        "description": "<p>前端版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ssid",
                        "description": "<p>ssid</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ssidPwd",
                        "description": "<p>ssidPwd</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"aliUpgrade\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"deviceId\":\"\",\n        \"algorighmVer\":\"\",\n        \"sdkVer\":\"\",\n        \"communityVer\":\"\",\n        \"firmwareVer\":\"\",\n        \"ssid\":\"\",\n        \"ssidPwd\":\"\",\n        \"frontVer\":\"\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=data",
        "title": "数据记录",
        "description": "<p>urlName: tracing  用户端软件或硬件数据记录</p>",
        "group": "tracing",
        "name": "dataTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "content",
                        "description": "<p>内容，一般是数据文件上传后的内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "files",
                        "description": "<p>文件，一般是数据文件上传后的dfsId，以逗号分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "others",
                        "description": "<p>其它，一般是数据相关的一些信息</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "source",
                        "description": "<p>来源</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"data\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\": {\n\t\t\"files\":\"xxx\",\n\t\t\"source\":\"xxx\",\n\t\t\"others\":\"xxx\"\n\t}\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=dot",
        "title": "软硬件功能点使用跟踪",
        "description": "<p>urlName: tracing  软硬件设置变动记录</p>",
        "group": "tracing",
        "name": "dotTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "dotName",
                        "description": "<p>功能点</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "modelCode",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"dot\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"dotName\":\"xxx\",\n        \"modelCode\":\"XXX\",\n        \"sn\":\"XXX\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=install",
        "title": "软硬件安装记录跟踪",
        "description": "<p>urlName: tracing  软硬件安装记录</p>",
        "group": "tracing",
        "name": "installTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "email",
                        "description": "<p>邮箱</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "phone",
                        "description": "<p>手机</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "title",
                        "description": "<p>称呼</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"install\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"email\":\"\",\n        \"phone\":\"\",\n        \"title\":\"\",\n        \"industry\":\"\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=log",
        "title": "log记录",
        "description": "<p>urlName: tracing  用户端软件或硬件日志记录</p>",
        "group": "tracing",
        "name": "logTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "content",
                        "description": "<p>内容，一般是日志文件上传后的内容，以逗号分隔</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"log\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":\"xxx\"\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=scan",
        "title": "扫描记录跟踪",
        "description": "<p>urlName: tracing  从新建、载入工程到保存操作记录</p>",
        "group": "tracing",
        "name": "scanTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": false,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "mode",
                        "description": "<p>扫描模式</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "classsify",
                        "description": "<p>模式类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": true,
                        "field": "tuntableSteps",
                        "description": "<p>转台步数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]String",
                        "optional": false,
                        "field": "alignMode",
                        "description": "<p>拼接模式</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hdr",
                        "description": "<p>双曝光</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "texture",
                        "description": "<p>启用纹理</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": true,
                        "field": "frameRate",
                        "description": "<p>帧数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": true,
                        "field": "totalPoint",
                        "description": "<p>点数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "pointDis",
                        "description": "<p>点距</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "handHeldPointGenWay",
                        "description": "<p>手持点云的方式</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "meshType",
                        "description": "<p>封装方式</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "box",
                        "description": "<p>数据尺寸</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "length",
                        "description": "<p>长</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "width",
                        "description": "<p>宽</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "height",
                        "description": "<p>高</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "fileName",
                        "description": "<p>文件名</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"scan\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"mode\":[{\n\t\t\t\"startOn\":\"2017-01-28T12:04:04Z\",\n\t\t\t\"endOn\":\"2017-01-28T12:04:04Z\",\n\t\t\t\"tuntableSteps\":44,\n\t\t\t\"alignMode\":[\n\t\t\t\t\"Markers\", \"Mixed\"\n\t\t\t],\n\t\t\t\"hdr\":\"yes\",,\n\t\t\t\"modular\": [{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}],\n\t\t\t\"classsify\":\"HandheldHD\"\n        }],\n        \"texture\":\"yes\",\n        \"totalPoint\":9000,\n        \"frameRate\":15,\n        \"pointDis\":900.88,\n\t\t\"handHeldPointGenWay\":\"quality\",\n\t\t\"meshType\":\"none\",\n\t\t\"fileName\":\"dasfds\",\n\t\t\"box\":{\n\t\t\t\"length\":44.34,\n\t\t\t\"width\":44.34,\n\t\t\t\"height\":44.34\n\t\t}\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=score",
        "title": "评分记录跟踪",
        "description": "<p>urlName: tracing  一次评分操作记录</p>",
        "group": "tracing",
        "name": "scoreTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "score",
                        "description": "<p>分数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "comment",
                        "description": "<p>评分备注</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "industry",
                        "description": "<p>评分人所在行业</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"score\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"score\":5,\n        \"comment\":\"fadsfasd\",\n        \"industry\":\"dddd\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=setting",
        "title": "软硬件设置记录跟踪",
        "description": "<p>urlName: tracing  软硬件设置变动记录</p>",
        "group": "tracing",
        "name": "settingTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "enableTracing",
                        "description": "<p>是否允许采集</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "other",
                        "description": "<p>其它设置，一般是软硬件中的设置界面上的参数的json对象字符串</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"setting\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"enableTracing\":\"\",\n        \"other\":\"\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=share",
        "title": "分享使用记录跟踪",
        "description": "<p>urlName: tracing  一次分享操作记录</p>",
        "group": "tracing",
        "name": "shareTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "target",
                        "description": "<p>分享目标</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "account",
                        "description": "<p>分享的目标账号</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"share\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"target\":\"3dzao\",\n        \"name\":\"fadsfasd\",\n        \"account\":\"dddd\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=calibration",
        "title": "标定使用记录跟踪",
        "description": "<p>urlName: tracing  从进入到退出标定界面的一次记录</p>",
        "group": "tracing",
        "name": "tracingCalibration",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": false,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "classsify",
                        "description": "<p>标定类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "result",
                        "description": "<p>该类标定结果</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"calibration\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":[{\n        \"classsify\":\"hd\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ],\n\t\t\"startOn\":\"2017-01-28T12:04:04Z\",\n\t\t\"endOn\":\"2017-01-29T12:04:04Z\",\n\t\t\"result\":\"success\"\n    }]\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=dentalScan",
        "title": "齿科扫描记录跟踪",
        "description": "<p>urlName: tracing  齿科设备的一次扫描记录</p>",
        "group": "tracing",
        "name": "tracingDentalScan",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号，与modularExt中的ple中必须要提供1个至少</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "preparation",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "occlusionType",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "scanObjectType",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "callSourceType",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "dentalNotation",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "caseCreatedTime",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gingivaScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "situScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ortho",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "manualAlign",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "modelEdit",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "fillHole",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "rangeScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mendScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "multiMendScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gPURebuild",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "3Party",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "textureScan",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "refPoints",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "articulator",
                        "description": ""
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "remoteScanMode",
                        "description": ""
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"dentalScan\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"preparation\":\"Crown\",\n        \"occlusionType\":\"None\",\n        \"scanObjectType\":\"Die\",\n        \"callSourceType\":\"DentalScan\",\n        \"dentalNotation\":\"FDI\",\n        \"caseCreatedTime\":\"2018-05-28T13:04:04Z\",\n        \"gingivaScan\":\"true\",\n        \"situScan\":\"false\",\n        \"ortho\":\"true\",\n        \"manualAlign\":\"false\",\n        \"modelEdit\":\"true\",\n        \"fillHole\":\"false\",\n        \"rangeScan\":\"true\",\n        \"mendScan\":\"false\",\n        \"multiMendScan\":\"true\",\n        \"gPURebuild\":\"false\",\n        \"3Party\":\"true\",\n        \"textureScan\":\"false\",\n        \"refPoints\":\"true\",\n        \"articulator\":\"false\",\n        \"remoteScanMode\":\"true\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=feedback",
        "title": "软硬件反馈记录跟踪",
        "description": "<p>urlName: tracing  软硬件反馈记录，会生成一个工单</p>",
        "group": "tracing",
        "name": "tracingFeedback",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "email",
                        "description": "<p>邮箱</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]String",
                        "optional": true,
                        "field": "attachs",
                        "description": "<p>附件</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"feedback\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"email\":\"\",\n        \"attachs\":[\"xxx\"],\n        \"content\":\"\",\n        \"industry\":\"\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=upgrade",
        "title": "升级记录跟踪",
        "description": "<p>urlName: upgrade  升级记录跟踪</p>",
        "group": "tracing",
        "name": "upgradeTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "content",
                        "description": "<p>采集内容，升级的版本</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"aliUpgrade\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":\"\"\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    },
    {
        "type": "post",
        "url": "/dtta?type=usage",
        "title": "软硬件使用记录跟踪",
        "description": "<p>urlName: tracing  软硬件从启动到关闭的一次记录</p>",
        "group": "tracing",
        "name": "usageTracing",
        "header": {
            "fields": {
                "Header": [
                    {
                        "group": "Header",
                        "type": "String",
                        "optional": false,
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
                        "optional": true,
                        "field": "modelName",
                        "description": "<p>软硬件名称，是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "serialNum",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installCode",
                        "description": "<p>本次安装时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "usageCode",
                        "description": "<p>本次启动时生成的唯一码</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareName",
                        "description": "<p>软件名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "softwareVer",
                        "description": "<p>是在型号管理中约定的唯一名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "tracingType",
                        "description": "<p>采集类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "isOnline",
                        "description": "<p>采集时是否联网,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "startOn",
                        "description": "<p>采集开始时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "endOn",
                        "description": "<p>采集结束时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osSoftExt",
                        "description": "<p>系统扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "osName",
                        "description": "<p>系统名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "hostName",
                        "description": "<p>主机名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osType",
                        "description": "<p>操作系统类型</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "osVersion",
                        "description": "<p>操作系统版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "lang",
                        "description": "<p>系统语言，来自标准的https://www.science.co.il/language/Locale-codes.php，codePage值或是LCID String</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "resolution",
                        "description": "<p>分辨率，以*分隔</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "installPath",
                        "description": "<p>安装路径，指电脑本地路径</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "browser",
                        "description": "<p>默认浏览器信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>默认浏览器名称</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ver",
                        "description": "<p>默认浏览器版本</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": false,
                        "field": "osHdExt",
                        "description": "<p>硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "cpu",
                        "description": "<p>cpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "cpuCores",
                        "description": "<p>cpu核数</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "cpuModel",
                        "description": "<p>cpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "cpuVendor",
                        "description": "<p>cpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": false,
                        "field": "gpu",
                        "description": "<p>gpu对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "gpuModel",
                        "description": "<p>gpu型号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "gpuMemSize",
                        "description": "<p>gpu内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "gpuVendor",
                        "description": "<p>gpu品牌</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "memSize",
                        "description": "<p>内存大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddSize",
                        "description": "<p>硬盘大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Integer",
                        "optional": false,
                        "field": "hddRemainSize",
                        "description": "<p>硬盘分区剩余大小，单位是byte</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "modularExt",
                        "description": "<p>配件或硬件扩展信息对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "ple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "[]Object",
                        "optional": true,
                        "field": "modular",
                        "description": "<p>模块对象</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "mple",
                        "description": "<p>加密串号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "validTo",
                        "description": "<p>有效期截止时间</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Bool",
                        "optional": true,
                        "field": "status",
                        "description": "<p>状态，是启用还是禁用状态,true/false</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "Object",
                        "optional": true,
                        "field": "content",
                        "description": "<p>采集内容</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "enableGuide",
                        "description": "<p>是否启用了引导</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n    \"modelName\":\"afinia_3d_einscan_s\",\n    \"serialNum\":\"\",\n    \"installCode\":\"xxx\",\n    \"usageCode\":\"xxx\",\n    \"softwareName\":\"einscan\",\n    \"softwareVer\":\"2.7.0.5\",\n    \"tracingType\":\"usage\",\n    \"isOnline\":true,\n    \"startOn\":\"2017-01-28T12:04:04Z\",\n    \"endOn\":\"2017-01-29T12:04:04Z\",\n    \"osSoftExt\":{\n        \"osName\":\"mac\",\n        \"hostName\":\"xxx\",\n        \"osType\":\"xxx\",\n        \"osVersion\":\"xxx\",\n        \"lang\":\"cn\",\n        \"resolution\":\"2478*1468\",\n        \"installPath\":\"afsdasd\",\n        \"browser\":{\n            \"name\":\"chrome\",\n            \"ver\":\"54.98\"\n        }\n    },\n    \"osHdExt\":{\n        \"cpu\":[{\n            \"cpuCores\":8,\n            \"cpuModel\":\"xeon\"\n        }],\n        \"memSize\":8096,\n        \"gpu\":[{\n            \"gpuModel\":\"intel hd4000\",\n            \"gpuMemSize\": 3900987777\n        }],\n        \"hddSize\":7866555,\n        \"hddRemainSize\":98792323232\n    },\n    \"modularExt\":{\n        \"ple\":\"588ea5a2b4fa8c29759e579d-V200.ple\",\n        \"modular\": [\n\t\t\t{\n\t\t\t\t\"name\":\"xxx\",\n\t\t\t\t\"sn\":\"xxx\",\n\t\t\t\t\"validTo\":\"xxx\",\n\t\t\t\t\"status\":false,\n\t\t\t\t\"mple\":\"xxx\"\n\t\t\t}\n        ]\n    },\n    \"content\":{\n        \"enableGuide\":\"\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "examples": [
                {
                    "title": "Success-Response",
                    "content": " {\n\t\"result\":\"\",\n\t\"status\":\"success\"\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "examples": [
                {
                    "title": "Error-Response",
                    "content": " {\n\t\"result\":\"xxx\",\n\t\"status\":\"fail\"\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/tracing.go",
        "groupTitle": "tracing"
    }
]

from jsonpath import jsonpath
from json import dumps,loads

def get_all_case(_apiInfo):
    title = _apiInfo.get("title", "")
    group = _apiInfo.get("group", "")
    url = _apiInfo.get("url", "")
    method = _apiInfo.get("type", "")
    data = jsonpath(_apiInfo, "$..parameter.examples..content")
    data = loads(data[0].replace(",,", ",")) if data else {}
    if method.lower() == "get":
        return ("采集微服务", group, title, url, method, dumps(data), "", "", "json", 200, "success")
    return ("采集微服务", group, title, url, method, "", "", dumps(data), "json", 200, "success")


if __name__ == '__main__':
    for i in apiInfo:
        print(get_all_case(i))
