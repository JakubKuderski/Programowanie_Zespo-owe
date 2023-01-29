import { Injectable } from '@nestjs/common'
import { CreateSettingDto } from './dto/create-setting.dto'
import { UpdateSettingDto } from './dto/update-setting.dto'
import { InjectModel } from '@nestjs/sequelize'
import { Layout } from './models/layout.model'
import { Social } from './models/social.model'

@Injectable()
export class SettingsService {
	constructor(
		@InjectModel(Layout)
		private layoutModel: typeof Layout,
		@InjectModel(Social)
		private socialModel: typeof Social,
	) {}

	create(createSettingDto: CreateSettingDto) {
		const layout = Layout.create({
			theme: createSettingDto.layout.theme,
		})
		const socials = createSettingDto.socials.map((social) => {
			return Social.create(social)
		})
		return {
			layout,
			socials: [...socials],
		}
	}

	findAll() {
		return `This action returns all settings`
	}

	findOne(id: number) {
		return `This action returns a #${id} setting`
	}

	update(id: number, updateSettingDto: UpdateSettingDto) {
		return `This action updates a #${id} setting`
	}

	remove(id: number) {
		return `This action removes a #${id} setting`
	}
}
