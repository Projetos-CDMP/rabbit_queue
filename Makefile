dcbuild:
	docker compose -f docker-compose.yml -f docker-compose.yml build
dcup:
	docker compose -f docker-compose.yml -f docker-compose.yml up -d

dcstop:
	docker compose -f docker-compose.yml -f docker-compose.yml stop

prune:
	docker system prune -a -f

dclogs:
	docker compose -f docker-compose.yml -f docker-compose.yml logs -f

remake:
	$(MAKE) dcstop && $(MAKE) prune && $(MAKE) dcup && $(MAKE) dclogs