SHELL=/bin/bash
INSTALL_DIR = ~/bin
FDL_TARGET = ${INSTALL_DIR}/find-dead-links.py
RUN_TARGET = ${INSTALL_DIR}/find-dead-links
FDL_ENV = ${INSTALL_DIR}/fdl-env

install: ${FDL_ENV} ${FDL_TARGET} ${RUN_TARGET}

${FDL_ENV}:
#	cd ${INSTALL_DIR} && virtualenv -p python3 ${FDL_ENV}
	virtualenv -p python3 ${FDL_ENV}
	source ${FDL_ENV}/bin/activate && pip install requests && pip install beautifulsoup4

${FDL_TARGET}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links.py

${RUN_TARGET}: find-dead-links
	cp find-dead-links ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links
