import s from './LoadedPhotoSingle.module.scss'
import {BaseButton} from 'common/components/BaseButton/BaseButton'
import React from 'react'
import {BaseFont} from 'common/components/BaseFont/BaseFont'
import {ReactComponent as DeleteIcon} from '../../../../assets/svg/delete.svg'

export interface ILoadedPhotoSingle {
	imageUri: string
	name: string
}

export const LoadedPhotoSingle: React.FC<ILoadedPhotoSingle> = ({imageUri, name}) => {
	return (
		<div className={s.loaded_photo}>
			<img src={imageUri} alt="Loaded photo"/>
			<div className={s.loaded_photo_overlay}>
				<BaseFont tag={'span'} color={'white'}>{name}</BaseFont>
				<BaseButton type={'primary'} icon={DeleteIcon} iconFill={'white'}>Delete photo</BaseButton>
			</div>
		</div>
	)
}