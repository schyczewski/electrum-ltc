from electrum_ltc.i18n import _

fullname = 'Ledger Wallet'
description = 'Provides support for Ledger hardware wallet'
requires = [('btchip', 'github.com/ledgerhq/btchip-python')]
#requires_wallet_type = ['btchip']
registers_keystore = ('hardware', 'btchip', _("Ledger wallet"))
available_for = ['qt', 'cmdline']
