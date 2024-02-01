# -*- coding: utf-8 -*-
import requests
import json
from google.protobuf.json_format import MessageToDict

from .sign import TiSign

defaultservice = "fusion-media-service"
defaultversion = "2022-03-02"
defaultgateway = "gateway"

service_map = {}
version_map = {}
gateway_map = {}

def unary_unary(request, cert, action, v1, v2, options, channel_credentials,
              insecure, call_credentials, compression, wait_for_ready, timeout, metadata):
  
  # 访问网关的host
  host = cert.host
  port = cert.port
  # 服务接口
  action = action.split('/')[2]
  # 接口版本
  version = defaultversion
  if action in version_map:
    version = version_map[action]

  # 接口所属服务
  service = defaultservice
  if action in service_map:
    service = service_map[action]
  
  gateway = defaultgateway
  if action in gateway_map:
    gateway = gateway_map[action]

  # http请求的content-type, 当前网关只支持: application/json  multipart/form-data
  conten_type = 'application/json'
  # http请求方法，当前网关只支持: POST GET
  http_method = 'POST'
  # Ti平台生成的鉴权密钥信息(通过 管理中心-个人中心-密钥管理 获取)
  secret_id = cert.secret_id
  secret_key = cert.secret_key

    # 创建TiSign对象
  ts = TiSign(host, action, version, service, conten_type,
              http_method, secret_id, secret_key)
  # 生成通过网关访问后端服务，所需http的请求header 和 签名信息
  http_header_dict, authorization = ts.build_header_with_signature()
  gateway_url = "http://" + host + ":" + str(port) + "/" + gateway
  if isinstance(request, dict):
    input = request.copy()
    input["TIProjectId"] = cert.ti_project_id
    input["TIBusinessId"] = cert.ti_business_id
  else:
    input = MessageToDict(request)
    input["TIProjectId"] = cert.ti_project_id
    input["TIBusinessId"] = cert.ti_business_id
  
  resp = requests.post(gateway_url, json=input, headers=http_header_dict)

  if resp.status_code != 200:
    print(resp.reason)
  else:
    print(json.dumps(json.loads(resp.content), ensure_ascii=False))

  return 1