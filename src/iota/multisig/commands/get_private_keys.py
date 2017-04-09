# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

import filters as f
from iota.commands import FilterCommand, RequestFilter
from iota.crypto.types import Seed
from iota.filters import Trytes

__all__ = [
  'GetPrivateKeysCommand',
]

class GetPrivateKeysCommand(FilterCommand):
  """
  Implements `get_private_keys` multisig API command.

  References:
    - :py:meth:`iota.multisig.MultisigIota.get_private_key`
    - https://github.com/iotaledger/wiki/blob/master/multisigs.md
  """
  command = 'getPrivateKeys'

  def get_request_filter(self):
    return GetPrivateKeysRequestFilter()

  def get_response_filter(self):
    pass

  def _execute(self, request):
    raise NotImplementedError(
      'Not implemented in {cls}.'.format(cls=type(self).__name__),
    )


class GetPrivateKeysRequestFilter(RequestFilter):
  def __init__(self):
    super(GetPrivateKeysRequestFilter, self).__init__(
      {
        # ``count`` and ``index`` are optional.
        'count':  f.Type(int) | f.Min(1) | f.Optional(default=1),
        'index':  f.Type(int) | f.Min(0) | f.Optional(default=0),

        'seed':   f.Required | Trytes(result_type=Seed),
      },

      allow_missing_keys = {
        'count',
        'index',
      },
    )
