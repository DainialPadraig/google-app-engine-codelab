#!/usr/bin/env python
#
# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS#!/usr/bin/env python
#
# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = 'appengine-support@google.com'

from google.appengine.ext import db


class WikiUser(db.Model):
  wiki_user = db.UserProperty()
  joined = db.DateTimeProperty(auto_now_add=True)
  wiki_user_picture = db.BlobProperty()
  user_feed = db.StringProperty()


class WikiContent(db.Model):
  title = db.StringProperty(required=True)


class WikiRevision(db.Model):
  wiki_page = db.ReferenceProperty(WikiContent)
  revision_body = db.TextProperty(required=True)
  author = db.ReferenceProperty(WikiUser)
  created = db.DateTimeProperty(auto_now_add=True)
  version_number = db.IntegerProperty()