# -*- coding: utf-8 -*-


class Cert:
  def __init__(self, host, port, secret_id, secert_key, ti_business_id, ti_project_id) -> None:
    self.host = host
    self.port = port
    if port == 0:
      self.port = 80
    self.secret_id = secret_id
    self.secret_key = secert_key
    self.ti_business_id = ti_business_id
    self.ti_project_id = ti_project_id