# coding:utf-8

false = False
true = True
apiInfo = [
    {
        "type": "post",
        "url": "/ed/apply",
        "title": "5加解密授权申请审核接口",
        "description": "<p>urlName: applyED 集成方在未激活、已注销但在有效期内时才能调用 \\</p> <ol> <li>如果未激活状态，则返回成功； \\</li> <li>如果已经申请但在审核中，同台设备提示审核中(waitingAudit)否则提示非法(illegal)； \\</li> <li>如果已经申请且待激活确认，同台设备则返回(waitActive)，集成方应该调用加解密授权激活下载及获取审核结果接口，非同台设备提示非法(illegal)； \\</li> <li>如果已激活且在有效期内，同台则提示(actived)，非同台设备提示非法(illegal)； \\</li> <li>如果已激活且不在有效期内，则返回成功； \\</li> <li>如果已注销且在有效期内，同台则返回成功，否则返回(waitActive)，集成方应该调用加解密授权激活下载及获取审核结果接口； \\</li> <li>如果已注销且不在有效期内，则返回成功； \\</li> <li>如果激活不存在，则返回(notExist); \\</li> <li>如果不是上述的值，则返回请求格式错误(http的statusCode是400)或者是未知错误(unknown) \\</li> <li>如果已不在有效期内，则返回成功；</li> </ol>",
        "group": "EncryptDecrypt",
        "name": "applyED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "deviceModelCode",
                        "description": "<p>约定的设备唯一型号名，比如einscan</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "deviceSN",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码，如果不是solidEdge则是设备的序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "name",
                        "description": "<p>姓名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "company",
                        "description": "<p>公司</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "telephone",
                        "description": "<p>电话</p>"
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
                        "field": "country",
                        "description": "<p>国家</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "addr",
                        "description": "<p>地址</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"sn\": \"xxxx\",\n\t\"fingerprint\":\"xxx\",\n\t\"deviceModelCode\": \"xxxx\",\n\t\"deviceSN\": \"xxxx\",\n\t\"industry\":\"xxx\",\n\t\"addr\":\"xxx\",\n\t\"country\":\"xxx\",\n\t\"email\":\"xxx\",\n\t\"telephone\":\"xxx\",\n\t\"company\":\"xxx\",\n\t\"name\":\"xxx\"\n}",
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
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "notExist",
                        "description": "<p>表示不存在，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "illegal",
                        "description": "<p>表示非法，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unknown",
                        "description": "<p>表示未知错误，挂在SN字段下</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"SN\\\":\\\"notExist\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    },
    {
        "type": "post",
        "url": "/ed/status",
        "title": "4加解密授权状态查询接口",
        "description": "<p>urlName: statusED 集成方在启动时调用，接口对sn、指纹、解密内容结合有效期、状态进行判断： \\</p> <ul> <li>unactived状态：调用激活申请接口 \\</li> <li>waitingAudit待审核中：提示用户，如果着急可以联系XXX \\</li> <li>waitActive：调用激活下载接口 \\</li> <li>notExist：提示用户并调用激活申请接口 \\</li> <li>inValid：表示已经注销，则可以调用激活申请接口 \\</li> <li>illegal：提示用户该序列号已经用在其它设备上 \\</li> <li>unknown：提示用户遇到问题，稍候再试 \\</li> <li>serverErr 表示服务器错误，稍候再试 \\</li> <li>拿到状态完整信息并保存本地</li> </ul>",
        "group": "EncryptDecrypt",
        "name": "statusED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>Optional SolidEdge的激活码或是设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "data",
                        "description": "<p>Optional 调用库生成的解密内容</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"sn\": \"xxxx\",\n\t\"fingerprint\":\"xxx\",\n\t\"data\":\"xxx\"\n}",
                    "type": "json"
                }
            ]
        },
        "success": {
            "fields": {
                "Success 200": [
                    {
                        "group": "Success 200",
                        "type": "Int",
                        "optional": false,
                        "field": "concurrent",
                        "description": "<p>允许的并发运行数量</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "createAt",
                        "description": "<p>第1次授权开始时间</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "validUntil",
                        "description": "<p>授权有效时间</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "Float",
                        "optional": false,
                        "field": "surplusDays",
                        "description": "<p>剩余有效天数</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "Int",
                        "optional": false,
                        "field": "upgradeCount",
                        "description": "<p>已经激活的次数</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "data",
                        "description": "<p>调用库生成的解密内容</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "modelCode",
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "deviceModelCode",
                        "description": "<p>约定的设备唯一型号名，比如einscan</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "deviceSN",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "version",
                        "description": "<p>版本信息</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码，如果不是solidEdge则是设备的序列号</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "name",
                        "description": "<p>姓名</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "company",
                        "description": "<p>公司</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "telephone",
                        "description": "<p>电话</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "email",
                        "description": "<p>邮箱</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "country",
                        "description": "<p>国家</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "addr",
                        "description": "<p>地址</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Success-Response",
                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\t\"modelCode\": \"xxxx\",\n\t\t\"sn\": \"xxxx\",\n\t\t\"fingerprint\":\"xxx\",\n\t\t\"data\":\"xxx\",\n\t\t\"concurrent\":1,\n\t\t\"createAt\":\"xxx\",\n\t\t\"validUntil\":\"xxx\",\n\t\t\"surplusDays\":0.00,\n\t\t\"upgradeCount\":0,\n\t\t\"version\":\"xxx\",\n\t\t\"deviceModelCode\": \"xxxx\",\n\t\t\"deviceSN\": \"xxxx\",\n\t\t\"industry\":\"xxx\",\n\t\t\"addr\":\"xxx\",\n\t\t\"country\":\"xxx\",\n\t\t\"email\":\"xxx\",\n\t\t\"telephone\":\"xxx\",\n\t\t\"company\":\"xxx\",\n\t\t\"name\":\"xxx\"\n\t}\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "notExist",
                        "description": "<p>表示不存在，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "waitActive",
                        "description": "<p>表示待激活，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "waitingAudit",
                        "description": "<p>表示审核中，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "inValid",
                        "description": "<p>表示已经过期，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "illegal",
                        "description": "<p>表示非法，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unactived",
                        "description": "<p>表示未激活，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unknown",
                        "description": "<p>表示未知错误，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在SN字段下</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"SN\\\":\\\"notExist\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    },
    {
        "type": "post",
        "url": "/ed/trailAccount",
        "title": "3加解密授权试用期客户信息录入接口",
        "description": "<p>urlName: trailAccountED 集成方在试用时提交用户录入的客户信息, 必须是试用未结束的情况下可以录入成功；字段错误提示用户修正，服务器错误(serverErr)则提示用户稍候再试，其它返回非法(illegal)，提示用户去激活；</p>",
        "group": "EncryptDecrypt",
        "name": "trailAccountED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "deviceModelCode",
                        "description": "<p>约定的设备唯一型号名，比如einscan</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "deviceSN",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码，如果不是solidEdge则是设备的序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "name",
                        "description": "<p>姓名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "company",
                        "description": "<p>公司</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "telephone",
                        "description": "<p>电话</p>"
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
                        "field": "country",
                        "description": "<p>国家</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "addr",
                        "description": "<p>地址</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"fingerprint\":\"xxx\",\n\t\"deviceModelCode\": \"xxxx\",\n\t\"deviceSN\": \"xxxx\",\n\t\"industry\":\"xxx\",\n\t\"addr\":\"xxx\",\n\t\"country\":\"xxx\",\n\t\"email\":\"xxx\",\n\t\"telephone\":\"xxx\",\n\t\"company\":\"xxx\",\n\t\"name\":\"xxx\"\n}",
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
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在fingerPrint字段下，需要客户端稍候重试，或是待服务端改正错误后再试</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "illegal",
                        "description": "<p>表示非法，挂在fingerPrint字段下，试用已经结束，提示用户去激活</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"fingerPrint\\\":\\\"illegal\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    },
    {
        "type": "post",
        "url": "/ed/trail",
        "title": "3加解密授权试用期状态查询接口",
        "description": "<p>urlName: trailED 集成方在启动时如果还没有激活码时调用： \\</p> <ol> <li>返回该fingerprint的首次试用登记时间、试用状态和试用剩余时间、是否已激活、首次激活时间； \\</li> <li>集成方如果收到已激活的信息，应该调用后面的激活状态查询接口获取更多信息； \\</li> <li>如果不是上述的值，则返回请求格式错误(http的statusCode是400)或者是未知错误(unknown) <br> 需要保存第1次的请求时间和每次的请求时间，用于判断试用时间</li> </ol>",
        "group": "EncryptDecrypt",
        "name": "trailED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"fingerprint\":\"xxx\"\n}",
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
                        "optional": false,
                        "field": "createAt",
                        "description": "<p>第1次试用开始时间</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "Float",
                        "optional": false,
                        "field": "surplusDays",
                        "description": "<p>剩余有效天数</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "modelCode",
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码或是设备序列号</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "actived",
                        "description": "<p>是否有激活记录，正常在试用期是不应该有的，否则表示此用户已经重装</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "deviceModelCode",
                        "description": "<p>约定的设备唯一型号名，比如einscan</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "deviceSN",
                        "description": "<p>设备序列号</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "name",
                        "description": "<p>姓名</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "company",
                        "description": "<p>公司</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "telephone",
                        "description": "<p>电话</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "email",
                        "description": "<p>邮箱</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "country",
                        "description": "<p>国家</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "addr",
                        "description": "<p>地址</p>"
                    },
                    {
                        "group": "Success 200",
                        "type": "String",
                        "optional": true,
                        "field": "industry",
                        "description": "<p>行业</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Success-Response",
                    "content": "{\n    \"status\": \"success\",\n    \"result\": {\n\t\t\"modelCode\": \"xxxx\",\n\t\t\"fingerprint\":\"xxx\",\n\t\t\"actived\":false,\n\t\t\"createAt\":\"xxx\",\n\t\t\"sn\":\"xxx\",\n\t\t\"surplusDays\":0.00,\n\t\t\"deviceModelCode\": \"xxxx\",\n\t\t\"deviceSN\": \"xxxx\",\n\t\t\"industry\":\"xxx\",\n\t\t\"addr\":\"xxx\",\n\t\t\"country\":\"xxx\",\n\t\t\"email\":\"xxx\",\n\t\t\"telephone\":\"xxx\",\n\t\t\"company\":\"xxx\",\n\t\t\"name\":\"xxx\"\n\t}\n}",
                    "type": "json"
                }
            ]
        },
        "error": {
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在fingerPrint字段下，需要客户端稍候重试，或是待服务端改正错误后再试</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unknown",
                        "description": "<p>表示未知错误，挂在fingerPrint字段下，需要客户端稍候重试，或是待服务端改正错误后再试</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"fingerprint\\\":\\\"notExist\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    },
    {
        "type": "post",
        "url": "/ed/version",
        "title": "2加解密授权版本信息反馈接口",
        "description": "<p>urlName: versionED 集成方在可以获取运行版本信息时反馈： <br> 需要保存第1次的请求时间和每次的请求时间，用于判断版本记录</p>",
        "group": "EncryptDecrypt",
        "name": "versionED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码或是设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "version",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "currentVersion",
                        "description": "<p>加解密集成方的版本信息，用于追溯问题</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": true,
                        "field": "data",
                        "description": "<p>调用库生成的解密内容</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"sn\": \"xxxx\",\n\t\"fingerprint\":\"xxx\",\n\t\"version\":\"xxx\",\n\t\"currentVersion\":\"xxx\",\n\t\"data\":\"xxx\"\n}",
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
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在FingerPrint字段下，需要客户端稍候重试，或是待服务端改正错误后再试</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unknown",
                        "description": "<p>表示未知错误，挂在FingerPrint字段下，需要客户端稍候重试，或是待服务端改正错误后再试</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"fingerPrint\\\":\\\"serverErr\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    },
    {
        "type": "post",
        "url": "/ed/withdraw",
        "title": "7加解密授权注销接口",
        "description": "<p>urlName: withdrawED 必须是已经激活状态, 序列号、fingerprint对上，才能申请提交成功；字段错误，服务器错误(serverErr)则稍候再试，其它返回非法(illegal)，提示用户</p>",
        "group": "EncryptDecrypt",
        "name": "withdrawED",
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
                        "description": "<p>约定的唯一型号名，比如solidEdge，一般是集成软件的约定名称或是产品线指定的设备唯一型号名</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "sn",
                        "description": "<p>SolidEdge的激活码或是设备序列号</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "fingerprint",
                        "description": "<p>SolidEdge运行电脑或是设备的指纹</p>"
                    },
                    {
                        "group": "Parameter",
                        "type": "String",
                        "optional": false,
                        "field": "data",
                        "description": "<p>调用库生成的解密内容</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Request-Example:",
                    "content": "{\n\t\"modelCode\": \"xxxx\",\n\t\"sn\": \"xxxx\",\n\t\"fingerprint\":\"xxx\",\n\t\"data\":\"xxx\"\n}",
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
            "fields": {
                "Error 4xx": [
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "serverErr",
                        "description": "<p>表示服务器错误，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "illegal",
                        "description": "<p>表示不合法，挂在SN字段下</p>"
                    },
                    {
                        "group": "Error 4xx",
                        "optional": false,
                        "field": "unknown",
                        "description": "<p>表示未知错误，挂在SN字段下</p>"
                    }
                ]
            },
            "examples": [
                {
                    "title": "Error-Response:",
                    "content": "{\n    \"status\": \"fail\",\n    \"result\": \"{\\\"SN\\\":\\\"illegal\\\"}\"\n    }\n}",
                    "type": "json"
                }
            ]
        },
        "version": "0.0.0",
        "filename": "services/ed.go",
        "groupTitle": "EncryptDecrypt"
    }
]

from jsonpath import jsonpath
from json import dumps, loads


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
