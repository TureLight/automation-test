/*
 Navicat Premium Data Transfer

 Source Server         : mongo
 Source Server Type    : MongoDB
 Source Server Version : 30608
 Source Host           : 192.168.1.6:27017
 Source Schema         : automation_data

 Target Server Type    : MongoDB
 Target Server Version : 30608
 File Encoding         : 65001

 Date: 29/03/2021 01:12:51
*/


// ----------------------------
// Collection structure for dashboard_data
// ----------------------------
db.getCollection("dashboard_data").drop();
db.createCollection("dashboard_data");

// ----------------------------
// Documents of dashboard_data
// ----------------------------
db.getCollection("dashboard_data").insert([ {
    _id: ObjectId("60560adee41a0000c4005e42"),
    "key_words": "task_data_list",
    "update_time": ISODate("1970-01-01T00:00:01.998Z"),
    "data_body": [
        {
            "task_name": "测试版本0.5.0",
            "submit_time": "2020-03-10",
            "run_time": "1天22小时33分",
            status: "done",
            "create_date": ISODate("1970-01-01T00:00:01.998Z")
        },
        {
            "task_name": "测试版本0.5.3",
            "submit_time": "2020-03-17",
            "run_time": "1天22小时33分",
            status: "running",
            "create_date": ISODate("1980-01-01T00:00:01.998Z")
        },
        {
            "task_name": "测试版本0.5.3",
            "submit_time": "2020-03-18",
            "run_time": "1天22小时33分",
            status: "waiting",
            "create_date": ISODate("1990-01-01T00:00:01.998Z")
        }
    ]
} ]);
db.getCollection("dashboard_data").insert([ {
    _id: ObjectId("60560e99e41a0000c4005e43"),
    "key_words": "panel_group_data",
    "update_time": ISODate("1970-01-01T00:00:01.998Z"),
    "data_body": {
        "case_num": NumberLong("199"),
        "task_case_num": NumberLong("99"),
        "run_time": "33天12小时33分",
        "task_progress": NumberLong("28")
    }
} ]);
db.getCollection("dashboard_data").insert([ {
    _id: ObjectId("60570724183000008e001132"),
    "key_words": "pie_chart_data",
    "update_time": ISODate("1970-01-01T00:00:01.998Z"),
    "data_body": [
        {
            value: NumberLong("600"),
            name: "成功"
        },
        {
            value: NumberLong("24"),
            name: "失败"
        },
        {
            value: NumberLong("88"),
            name: "错误"
        },
        {
            value: NumberLong("102"),
            name: "跳过"
        }
    ]
} ]);
db.getCollection("dashboard_data").insert([ {
    _id: ObjectId("60570b12183000008e001133"),
    "key_words": "bar_chart_data",
    "update_time": ISODate("1970-01-01T00:00:01.998Z"),
    "data_body": {
        "success_list": [
            79,
            52,
            200,
            334,
            390
        ],
        "failed_list": [
            79,
            52,
            200,
            334,
            390
        ],
        "error_list": [
            79,
            52,
            200,
            334,
            390
        ],
        "skip_list": [
            79,
            52,
            200,
            334,
            390
        ]
    }
} ]);

// ----------------------------
// Collection structure for task_schedule
// ----------------------------
db.getCollection("task_schedule").drop();
db.createCollection("task_schedule");

// ----------------------------
// Documents of task_schedule
// ----------------------------
db.getCollection("task_schedule").insert([ {
    _id: ObjectId("6060b5954f18b1c693fc56b5"),
    id: NumberLong("2"),
    "update_time": "2021-03-29 01:09",
    total: NumberLong("55"),
    "task_name": "测试增加",
    "suite_name": "bbtg",
    operator: "谭文景",
    version: "0.1.1",
    status: "idle",
    "f_key": "60608a95a22b86f7ea5c317e",
    "is_delete": false,
    "p_key": "6060b5954f18b1c693fc56b5"
} ]);
db.getCollection("task_schedule").insert([ {
    _id: ObjectId("6060b5f64f18b1c693fc56b6"),
    id: NumberLong("3"),
    "update_time": "2021-03-29 01:08",
    total: NumberLong("12"),
    "task_name": "测试增加2",
    "suite_name": "1234",
    operator: "常欣怡",
    version: ".01.3",
    status: "idle",
    "f_key": "606087562f667d0c9b45a92f",
    "is_delete": false,
    "p_key": "6060b5f64f18b1c693fc56b6"
} ]);

// ----------------------------
// Collection structure for test_case
// ----------------------------
db.getCollection("test_case").drop();
db.createCollection("test_case");

// ----------------------------
// Documents of test_case
// ----------------------------
db.getCollection("test_case").insert([ {
    _id: ObjectId("60576b63183000008e001134"),
    id: NumberLong("1"),
    "update_time": "2021-03-27 12:46",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "周春花",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("35"),
    "p_key": "60576b63183000008e001134"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605e20da3c310000b7003663"),
    id: NumberLong("2"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "605e20da3c310000b7003663"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605e20e13c310000b7003664"),
    id: NumberLong("3"),
    "update_time": "2021-03-27 03:10",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "李伦鑫",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("15"),
    "p_key": "605e20e13c310000b7003664"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ebbde05d0e745651dde2e"),
    "update_time": "2021-03-27 13:44",
    "module_name": "1",
    "file_name": "1",
    "file_path": "1222222",
    author: "常欣怡",
    version: "1",
    status: "done",
    "is_delete": false,
    id: NumberLong("4"),
    "p_key": "605ebbde05d0e745651dde2e",
    total: NumberLong("1")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ebe4d05d0e745651dde2f"),
    "update_time": "2021-03-27 13:10",
    "module_name": "2",
    "file_name": "3",
    "file_path": "222",
    author: "常欣怡",
    version: "1",
    status: "done",
    "is_delete": false,
    id: NumberLong("5"),
    "p_key": "605ebe4d05d0e745651dde2f",
    total: NumberLong("2")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ebed405d0e745651dde30"),
    "update_time": "2021-03-27 13:12",
    "module_name": "2",
    "file_name": "3",
    "file_path": "56",
    author: "常欣怡",
    version: "5",
    status: "done",
    "is_delete": false,
    id: NumberLong("6"),
    "p_key": "605ebed405d0e745651dde30",
    total: NumberLong("4")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ec010b5a9a4fe95216f0e"),
    id: NumberLong("7"),
    "update_time": "2021-03-27 13:18",
    "module_name": "2",
    "file_name": "3",
    "file_path": "5",
    author: "常欣怡",
    version: "5",
    status: "done",
    "is_delete": false,
    "p_key": "605ec010b5a9a4fe95216f0e",
    total: NumberLong("6")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ec03ab5a9a4fe95216f0f"),
    id: NumberLong("8"),
    "update_time": "2021-03-27 13:44",
    "module_name": "333",
    "file_name": "333",
    "file_path": "333",
    author: "谭文景",
    version: "333222",
    status: "done",
    "is_delete": false,
    "p_key": "605ec03ab5a9a4fe95216f0f",
    total: NumberLong("99")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605ec64fb5a9a4fe95216f10"),
    id: NumberLong("9"),
    "update_time": "2021-03-27 17:47",
    "module_name": "cc",
    "file_name": "zz",
    "file_path": "zz",
    author: "张信",
    version: "zzzzzz",
    status: "done",
    "is_delete": false,
    "p_key": "605ec64fb5a9a4fe95216f10",
    total: NumberLong("11")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605edd6db5a9a4fe95216f11"),
    id: NumberLong("10"),
    "update_time": "2021-03-27 17:46",
    "module_name": "333",
    "file_name": "333",
    "file_path": "333",
    author: "谭文景",
    version: "3333",
    status: "coding",
    "is_delete": true,
    "p_key": "605edd6db5a9a4fe95216f11",
    total: NumberLong("222")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605f4917a7b7bc9cb3e0cfba"),
    id: NumberLong("11"),
    "update_time": "2021-03-27 23:02",
    "module_name": "测试",
    "file_name": "测试",
    "file_path": "测试",
    author: "李伦鑫",
    version: "0.1.0",
    status: "coding",
    "is_delete": false,
    "p_key": "605f4917a7b7bc9cb3e0cfba",
    total: NumberLong("333")
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("605f4a339416ed3dce2aec1c"),
    id: NumberLong("12"),
    "update_time": "2021-03-27 23:07",
    total: NumberLong("77"),
    "module_name": "77",
    "file_name": "77",
    "file_path": "77",
    author: "常欣怡",
    version: "777",
    status: "done",
    "is_delete": false,
    "p_key": "605f4a339416ed3dce2aec1c"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060503513000000e1007e12"),
    id: NumberLong("13"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060503513000000e1007e12"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060504213000000e1007e13"),
    id: NumberLong("14"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060504213000000e1007e13"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060504613000000e1007e14"),
    id: NumberLong("15"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060504613000000e1007e14"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060504a13000000e1007e15"),
    id: NumberLong("25"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060504a13000000e1007e15"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060504e13000000e1007e16"),
    id: NumberLong("26"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060504e13000000e1007e16"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060505113000000e1007e17"),
    id: NumberLong("27"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060505113000000e1007e17"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060505513000000e1007e18"),
    id: NumberLong("28"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060505513000000e1007e18"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060505713000000e1007e19"),
    id: NumberLong("29"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060505713000000e1007e19"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060506913000000e1007e1a"),
    id: NumberLong("20"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060506913000000e1007e1a"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060506c13000000e1007e1b"),
    id: NumberLong("21"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060506c13000000e1007e1b"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060506f13000000e1007e1c"),
    id: NumberLong("22"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060506f13000000e1007e1c"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("6060508b13000000e1007e1d"),
    id: NumberLong("23"),
    "update_time": "123456",
    "module_name": "宏观框架",
    "file_name": "test_module",
    "file_path": "./test_case/test.py",
    author: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    total: NumberLong("20"),
    "p_key": "6060508b13000000e1007e1d"
} ]);
db.getCollection("test_case").insert([ {
    _id: ObjectId("60608af9a22b86f7ea5c3180"),
    id: NumberLong("30"),
    "update_time": "2021-03-28 21:56",
    total: NumberLong("22"),
    "module_name": "1llll",
    "file_name": "llll",
    "file_path": "lll",
    author: "常欣怡",
    version: "llll",
    status: "done",
    "is_delete": false,
    "p_key": "60608af9a22b86f7ea5c3180"
} ]);

// ----------------------------
// Collection structure for test_suite
// ----------------------------
db.getCollection("test_suite").drop();
db.createCollection("test_suite");

// ----------------------------
// Documents of test_suite
// ----------------------------
db.getCollection("test_suite").insert([ {
    _id: ObjectId("605f42321f220000b2005602"),
    id: NumberLong("1"),
    "update_time": "2021-03-28 21:53",
    total: NumberLong("35"),
    "suite_name": "test_module",
    tester: "张信",
    version: "0.5.0",
    status: "done",
    "is_delete": false,
    "p_key": "605f42321f220000b2005602",
    "case_keys": [
        "60576b63183000008e001134",
        "605e20da3c310000b7003663",
        "605e20e13c310000b7003664",
        "605ebbde05d0e745651dde2e"
    ]
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("60602392d8665edae8d57d42"),
    id: NumberLong("2"),
    "update_time": "2021-03-28 21:47",
    "suite_name": "22233",
    tester: "周春花",
    version: "222334444",
    "is_delete": true,
    "p_key": "60602392d8665edae8d57d42",
    "case_keys": "[]",
    status: "idle",
    total: 55
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("606026b376d3070251e823e6"),
    id: NumberLong("3"),
    "update_time": "2021-03-28 21:32",
    "suite_name": "44",
    tester: "44",
    version: "44",
    "is_delete": true,
    "p_key": "606026b376d3070251e823e6",
    "case_keys": "[]",
    status: "idle",
    total: 55
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("606087562f667d0c9b45a92f"),
    id: NumberLong("4"),
    "update_time": "2021-03-28 22:18",
    "suite_name": "1234",
    tester: "常欣怡",
    version: "ddddd",
    "case_keys": [
        "605ebe4d05d0e745651dde2f",
        "605ebed405d0e745651dde30",
        "605ec010b5a9a4fe95216f0e"
    ],
    "is_delete": false,
    "p_key": "606087562f667d0c9b45a92f",
    total: NumberLong("12"),
    status: "idle"
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("60608906a22b86f7ea5c317d"),
    id: NumberLong("5"),
    "update_time": "2021-03-28 22:19",
    "suite_name": "cd",
    tester: "谭文景",
    version: "aa0.1",
    "case_keys": [
        "60576b63183000008e001134",
        "605e20da3c310000b7003663",
        "605e20e13c310000b7003664",
        "605ebbde05d0e745651dde2e",
        "605ebe4d05d0e745651dde2f",
        "605ebed405d0e745651dde30",
        "605ec010b5a9a4fe95216f0e",
        "605ec03ab5a9a4fe95216f0f",
        "605ec64fb5a9a4fe95216f10",
        "605f4917a7b7bc9cb3e0cfba",
        "605f4a339416ed3dce2aec1c",
        "6060503513000000e1007e12",
        "6060504213000000e1007e13",
        "6060504613000000e1007e14",
        "6060504a13000000e1007e15",
        "6060504e13000000e1007e16",
        "6060505113000000e1007e17",
        "6060505513000000e1007e18",
        "6060505713000000e1007e19",
        "6060506913000000e1007e1a",
        "6060506c13000000e1007e1b",
        "6060506f13000000e1007e1c",
        "6060508b13000000e1007e1d",
        "60608af9a22b86f7ea5c3180"
    ],
    "is_delete": false,
    "p_key": "60608906a22b86f7ea5c317d",
    total: NumberLong("865"),
    status: "idle"
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("60608a95a22b86f7ea5c317e"),
    id: NumberLong("6"),
    "update_time": "2021-03-28 21:54",
    "suite_name": "bbtg",
    tester: "谭文景",
    version: "1.0",
    "case_keys": [ ],
    "is_delete": false,
    "p_key": "60608a95a22b86f7ea5c317e",
    status: "idle",
    total: 55
} ]);
db.getCollection("test_suite").insert([ {
    _id: ObjectId("60608adba22b86f7ea5c317f"),
    id: NumberLong("7"),
    "update_time": "2021-03-28 21:55",
    "suite_name": "lll",
    tester: "常欣怡",
    version: "1.3",
    "case_keys": [ ],
    "is_delete": false,
    "p_key": "60608adba22b86f7ea5c317f",
    status: "idle",
    total: 55
} ]);

// ----------------------------
// Collection structure for user_info
// ----------------------------
db.getCollection("user_info").drop();
db.createCollection("user_info");

// ----------------------------
// Documents of user_info
// ----------------------------
db.getCollection("user_info").insert([ {
    _id: ObjectId("6056393bd1f66ce41ad57736"),
    username: "zhangxin",
    password: "$2b$12$IHu9SapmWhxmISPEW.u0m.TjubF10sPeF2Mq6BUksm.LJzcgvSNJW",
    "full_name": "张信",
    "create_time": ISODate("2021-03-21T02:04:43.344Z"),
    "update_time": ISODate("2021-03-21T02:04:43.344Z"),
    roles: [
        "admin"
    ],
    "is_activate": true,
    "is_superuser": false
} ]);
db.getCollection("user_info").insert([ {
    _id: ObjectId("605642ae10535495e5676a4a"),
    username: "zhangxin1",
    password: "$2b$12$/cOwaeRB9.vSEjfuZ1KJs.gjI8NoTixHBvmIRw45ZiOxXLPphChHK",
    "full_name": "zx1",
    "create_time": ISODate("2021-03-21T02:45:02.054Z"),
    "update_time": ISODate("2021-03-21T02:45:02.054Z"),
    roles: [
        "admin"
    ],
    "is_activate": false,
    "is_superuser": false
} ]);
