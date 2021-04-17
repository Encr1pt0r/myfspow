#!/bin/sh

# listNotOverridden.sh

# list methods in FspowVisitor.py not overridden in FspowVisitorUser.py

GENFILE='FspowVisitor.py'
USRFILE='FspowVisitorUser.py'
GENTMP=listNotOverridden_gen_`date "+%Y%m%d%H%M%S"`
USRTMP=listNotOverridden_usr_`date "+%Y%m%d%H%M%S"`

grep "^\s*def" $USRFILE | awk -F 'def' '{print $2}' | cut -d'(' -f1 | sort >$USRTMP
grep "^\s*def" $GENFILE | awk -F 'def' '{print $2}' | cut -d'(' -f1 | sort >$GENTMP


# grep "^\s*def" $USRFILE | sort >$USRTMP
# grep "^\s*def" $GENFILE | sort >$GENTMP

echo "Methods in $GENFILE not overridden in $USRFILE:"
comm -23 $GENTMP $USRTMP

rm $USRTMP $GENTMP
