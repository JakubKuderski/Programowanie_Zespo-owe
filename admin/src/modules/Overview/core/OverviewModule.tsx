import React from 'react'
import {Module} from 'common/core/Module/Module'
import {ReactComponent as Icon} from 'assets/svg/overview.svg'
import {OverviewPage} from 'modules/Overview/pages/OverviewPage/OverviewPage'

export class OverviewModule extends Module {
	static defaultPath = '/'
	static moduleName = 'Overview'
	static icon = Icon

	registerRoutes(): void {
		this.routes.push(
			{
				path: '/',
				element: <OverviewPage />,
				name: 'Overview Page',
				description: 'Overview page description',
				title: 'Overview'
			}
		)
	}
}